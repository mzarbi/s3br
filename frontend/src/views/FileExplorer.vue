<template>
    <div class="row">
        <div class="col-12">
            <ribbon-panel
                :last_updated="last_updated"
                :selected_files="selected_files"
                @on-filter-by-type="filter_by_type"
                @on-filter-by-size="filter_by_size"
                @on-filter-by-date="filter_by_date"
                @on-filter-by-bookmarks="on_filter_by_bookmarks"
                @on-refresh="refresh"
            ></ribbon-panel>
            <div class="fancytree-grid-container flexbox-item-grow" style="height: 650px">
                <table id="treetable" width="100%">
                    <!-- <caption>Loading&hellip;</caption> -->
                    <colgroup>
                        <col width="10px">
                        <col width="1000px">
                        <col width="50px">
                        <col width="100px">
                    </colgroup>
                    <thead>
                    <tr>
                        <th width="10px"></th>
                        <th class="parent-path">
                            <nav class="navbar justify-content-between" style="box-shadow: none;">
                                <span id="breadcamp1"></span>
                                <span class="matches"></span>
                                <form class="form-inline input-group-sm" style="width: 60%;">

                                    <input class="form-control mr-sm-2" type="text" id="search-elem"
                                           name="search" incremental placeholder="Search text" autocomplete="off">
                                </form>
                            </nav>
                        </th>
                        <th>Size (bytes)</th>
                        <th>Last Modified</th>
                    </tr>
                    </thead>
                </table>
                <div id="verticalScrollbar" style="top:19px; height:calc(100% - 18px);"></div>
            </div>
        </div>
    </div>
</template>

<script>
    /* eslint-disable no-unused-vars */
    import $ from 'jquery';
    import RibbonPanel from "./file_explorer/RibbonPanel";

    import "jquery.fancytree/dist/modules/jquery.fancytree.ui-deps.js" ;
    import "jquery.fancytree/dist/modules/jquery.fancytree.js";
    import 'jquery.fancytree/dist/skin-lion/ui.fancytree.less';
    import "jquery.fancytree/dist/modules/jquery.fancytree.ariagrid.js";
    import "jquery.fancytree/dist/modules/jquery.fancytree.filter.js";
    import "jquery.fancytree/dist/modules/jquery.fancytree.grid.js";
    import "jquery.fancytree/dist/modules/jquery.fancytree.logger.js";
    import "jquery.fancytree/dist/modules/jquery.fancytree.childcounter.js";
    import PlainScrollbar from "../assets/PlainScrollbar/plain-scrollbar";

    export default {
        name: "FileExplorer",
        components: {
            RibbonPanel
        },
        data() {
            return {
                last_updated : "",
                showFileDetails : false,
                showFilePreview : false,
                selected_file :{},
                selected_files :[],
                hide_file_controls : true,
                hide_selection_controls : true

            };
        },
        created() {
            this.get_last_updated();
            this.build_file_system_tree();

        },
        methods: {
            build_file_system_tree(){
                const this_ = this;

                $(function () {
                    $("#optionsForm [name=cellFocus]").change(function (e) {
                        var value = $(this).find(":selected").val();

                        window.sessionStorage.setItem("cellFocus", value);
                        $.ui.fancytree.getTree("#treegrid").setOption("ariagrid.cellFocus", value);
                    }).val(window.sessionStorage.getItem("cellFocus") || "allow");

                    var modelCount = 0;

                    var sourceUrl = this_.$store.state.api_url + 'serve-file-structure';


                    $("#treetable").fancytree({
                        extensions: ["filter", "grid", "ariagrid", "childcounter"],
                        checkbox: true,
                        quicksearch: true,
                        autoScroll: true,
                        debugLevel: 3,
                        selectMode: 3,

                        ariagrid: {
                            // Internal behavior flags
                            activateCellOnDoubelclick: true,
                            cellFocus: $("#optionsForm [name=cellFocus]").find(":selected").val(),
                            label: "Tree Grid", // Added as `aria-label` attribute
                        },
                        childcounter: {
                            deep: true,
                            hideZeros: true,
                            hideExpanded: true
                        },
                        filter: {
                            autoExpand: true,
                        },
                        table: {
                            indentation: 20,       // indent 20px per node level
                            nodeColumnIdx: 1,      // render the node title into the 2nd column
                            checkboxColumnIdx: 0,  // render the checkboxes into the 1st column
                        },
                        viewport: {
                            enabled: true,
                            count: 15,
                        },
                        source: {
                            url: sourceUrl,
                            cache: true,
                        },
                        preInit: function(event, data) {
                            var tree = data.tree;

                            tree.verticalScrollbar = new PlainScrollbar({
                                alwaysVisible: true,
                                arrows: true,
                                orientation: "vertical",
                                onSet: function(numberOfItems) {
                                    tree.debug("verticalScrollbar:onSet", numberOfItems);
                                    tree.setViewport({
                                        start: Math.round(numberOfItems.start),
                                        // count: tree.viewport.count,
                                    });
                                },
                                scrollbarElement: document.getElementById("verticalScrollbar"),
                            });

                        },
                        init: function (event, data) {
                            modelCount = data.tree.count();
                            $("#treetable caption").text("Loaded " + modelCount + " nodes.");
                            data.tree.adjustViewportSize();

                        },
                        select: function(event, data) {
                            var selected_files_count = data.tree.getSelectedNodes().length;
                            if(selected_files_count === 0){

                                // clear selected files text
                                $("#selected_files").text("");

                                // hide selections controls
                                this_.hide_file_controls = true
                                this_.hide_selection_controls = true;

                                this_.selected_files = [];

                            }else{

                                // update selected files text
                                $("#selected_files").text("Selected Files : " + selected_files_count);

                                if(selected_files_count === 1){

                                    this_.hide_file_controls = false;
                                    this_.hide_selection_controls = false;
                                    this_.selected_file = data.tree.getSelectedNodes()[0];
                                }else{
                                    this_.hide_selection_controls = false;
                                    this_.selected_file = data.tree.getSelectedNodes();
                                }
                                this_.selected_files = data.tree.getSelectedNodes();
                            }

                        },
                        lazyLoad: function (event, data) {
                            data.result = {url: "ajax-sub2.json"}
                        },
                        activateCell: function (event, data) {
                            data.node.debug(event.type, data);
                        },
                        defaultGridAction: function (event, data) {
                            // Called when ENTER is pressed in cell-mode.
                            data.node.debug(event.type, data);
                        },
                        renderColumns: function (event, data) {
                            var node = data.node, $tdList = $(node.tr).find(">td");
                            // (index #2 is rendered by fancytree)
                            $tdList.eq(2).text(node.data.qty);
                            // $tdList.eq(3).text(node.data.qty);
                        },
                        updateViewport: function (event, data) {
                            var tree = data.tree,
                                topNode = tree.visibleNodeList[tree.viewport.start],
                                path = (topNode && !topNode.isTopLevel()) ? topNode.getPath(false) + "/..." : "";

                            tree.debug(event.type, data);

                            // Display breadcrumb/parent-path in header
                            //tree.$container.find("#breadcamp1").text(path);

                            tree.$container.find("#breadcamp1").html("");

                            $('<a class="navbar-brand" >' + path + '</a>').on({
                                click: function() {
                                    alert("hoi");
                                }
                            }).appendTo("#breadcamp1");

                            // Handle PlainScrollbar events
                            tree.verticalScrollbar.set({
                                start: tree.viewport.start,
                                total: tree.visibleNodeList.length,
                                visible: tree.viewport.count,
                            }, true);  // do not trigger `onSet`

                        },
                    });

                    $(window).on("resize", function (e) {
                        var tree = $.ui.fancytree.getTree();
                        tree.adjustViewportSize();
                    }).resize();

                    /* Handle inputs */
                    $(document).on("change", "#vpStart,#vpCount", function (e) {
                        var tree = $.ui.fancytree.getTree(),
                            opts = {
                                start: $("#vpStart").val(),
                                count: $("#vpCount").val(),
                            };

                        tree.setViewport(opts);
                    });

                    var timerid;
                    $("#search-elem").on("input", function(e) {
                        var value = $(this).val();
                        if ($(this).data("lastval") != value) {

                            $(this).data("lastval", value);
                            clearTimeout(timerid);

                            timerid = setTimeout(function() {

                                var n,
                                    tree = $.ui.fancytree.getTree(),
                                    match = $.trim(value);
                                // Pass a string to perform case insensitive matching
                                n = tree.filterNodes(match, {mode: "hide"});

                                $("span.matches").text(n ? "(" + n + " matches)" : "");
                            }, 500);
                        };
                    });
                });
            },
            get_last_updated(){
                const this_ = this;
                this.$axios
                    .get(this.$store.state.api_url + 'last-updated')
                    .then(response => {
                        this_.last_updated = response.data.last_updated;
                    })
            },
            refresh(){
                $.ui.fancytree.getTree().clearFilter();
            },

            on_filter_by_bookmarks(n){
                $.ui.fancytree.getTree().filterNodes(function(node) {
                    return n.includes(node.title)
                });
            },
            filter_by_date(n){
                $.ui.fancytree.getTree().filterNodes(function(node) {
                    var d = false;
                    if(n.after){
                        d = d || node.data.last_modified <= n.after_value;
                    }
                    if(n.before){
                        d = d || node.data.last_modified >= n.before_value;
                    }
                    return d;
                });
            },
            filter_by_size(n){
                $.ui.fancytree.getTree().filterNodes(function(node) {
                    var d = false;
                    if(n.lesser){
                        d = d || node.data.size <= n.lesser_value;
                    }
                    if(n.bigger){
                        d = d || node.data.size >= n.bigger_value;
                    }
                    return d;
                });
            },
            filter_by_type(n){
                $.ui.fancytree.getTree().filterNodes(function(node) {
                    var d = false;
                    if(n.csv){
                        d = d || node.title.endsWith("csv") === true;
                    }
                    if(n.xlsx){
                        d = d || node.title.endsWith("xlsx") === true;
                    }
                    if(n.parquet){
                        d = d || node.title.endsWith("parquet") === true;
                    }
                    if(n.txt){
                        d = d || node.title.endsWith("txt") === true;
                    }
                    if(n.json){
                        d = d || node.title.endsWith("json") === true;
                    }
                    return d;
                });
            }
        }
    };
</script>
