<template>
    <div id="ribbon">
        <div class="ribbon-window-title"></div>
        <div class="ribbon-tab" id="format-tab">
            <span class="ribbon-title">File</span>
            <div class="ribbon-section">
                <span class="section-title"></span>
                <details-ribbon-button
                        :not-available="hide_file_controls"
                        :selected_file="selected_file"
                        icon="list.png"
                ></details-ribbon-button>

                <preview-ribbon-button
                        :not-available="hide_file_controls"
                        :selected_file="selected_file"
                        icon="search.png"
                ></preview-ribbon-button>

                <s3-key-ribbon-button
                        :not-available="hide_file_controls"
                        :selected_file="selected_file"
                        icon="server.png"
                ></s3-key-ribbon-button>
            </div>
            <div class="ribbon-section">
                <span class="section-title">Users</span>
                <access-log-ribbon-button
                        :not-available="hide_file_controls"
                        :selected_file="selected_file"
                        icon="log-file.png"
                ></access-log-ribbon-button>
            </div>
            <div class="ribbon-section">
                <span class="section-title">Edit</span>
                <ribbon-button
                        :not-available="true"
                        option_name="Edit Name"
                        :selected_file="selected_file"
                        icon="id-card.png"
                ></ribbon-button>

                <ribbon-button
                        :not-available="true"
                        option_name="Replace"
                        :selected_file="selected_file"
                        icon="alter.png"
                ></ribbon-button>

                <ribbon-button
                        :not-available="true"
                        option_name="Move To"
                        :selected_file="selected_file"
                        icon="package.png"
                ></ribbon-button>
            </div>

            <div class="ribbon-section">
                <span class="section-title">Data</span>
                <columns-ribbon-button
                        :not-available="hide_file_controls"
                        :selected_file="selected_file"
                        icon="vertical.png"
                        btn_cls="ribbon-button-small"
                ></columns-ribbon-button>

                <extract-columns-ribbon-button
                        :not-available="true"
                        :selected_file="selected_file"
                        icon="table_1.png"
                        btn_cls="ribbon-button-small"
                ></extract-columns-ribbon-button>

            </div>

            <div class="ribbon-section">
                <span class="section-title">Bookmarks</span>
                <add2-bookmarks-ribbon-button
                        :not-available="hide_file_controls"
                        :selected_file="selected_file"
                        icon="book_1.png"
                        btn_cls="ribbon-button-small"
                ></add2-bookmarks-ribbon-button>
            </div>

        </div>
        <div class="ribbon-tab" id="reports-tab">
            <span class="ribbon-title">View</span>
            <div class="ribbon-section">
                <span class="section-title"></span>
                <modal-less-ribbon-button
                        :not-available="false"
                        :selected_file="selected_file"
                        icon="refresh.png"
                        option_name="Refresh"
                        @on-btn-clicked="refresh_clicked"
                ></modal-less-ribbon-button>
            </div>

            <div class="ribbon-section">
                <span class="section-title">Filters</span>
                <filter-by-type-ribbon-button
                        :not-available="false"
                        icon="extension.png"
                        @on-btn-clicked="filter_by_type"
                ></filter-by-type-ribbon-button>

                <filter-by-size-ribbon-button
                        :not-available="false"
                        icon="file.png"
                        @on-btn-clicked="filter_by_size"
                ></filter-by-size-ribbon-button>

                <filter-byd-a-t-e-ribbon-button
                        :not-available="false"
                        icon="calendar.png"
                        @on-btn-clicked="filter_by_date"
                ></filter-byd-a-t-e-ribbon-button>

                <ribbon-button
                        :not-available="true"
                        option_name="Lookup Table"
                        :selected_file="selected_file"
                        icon="table.png"
                ></ribbon-button>

            </div>

            <div class="ribbon-section">
                <span class="section-title">Bookmarks</span>
                <all-bookmarks-ribbon-button
                        :not-available="false"
                        icon="book.png"
                        @on-btn-clicked="filter_by_bookmarks"
                ></all-bookmarks-ribbon-button>


            </div>

            <div class="ribbon-section">
                <span class="section-title"></span>
                <ribbon-button
                        :not-available="true"
                        option_name="Settings"
                        :selected_file="selected_file"
                        icon="settings.png"
                ></ribbon-button>
            </div>
        </div>
        <div class="ribbon-tab" id="admin-tab">
            <div class="ribbon-section">
                <span class="section-title">Export</span>
                <modal-less-ribbon-button
                        :not-available="hide_selection_controls"
                        :selected_file="selected_file"
                        icon="export.png"
                        option_name="Download"
                        @on-btn-clicked="download_raw"
                ></modal-less-ribbon-button>

                <modal-less-ribbon-button
                        :not-available="hide_selection_controls"
                        :selected_file="selected_file"
                        icon="csv.png"
                        option_name="As csv"
                        @on-btn-clicked="download_as_csv"
                ></modal-less-ribbon-button>

                <modal-less-ribbon-button
                        :not-available="hide_selection_controls"
                        :selected_file="selected_file"
                        icon="xlsx.png"
                        option_name="As xlsx"
                        @on-btn-clicked="download_as_xlsx"
                ></modal-less-ribbon-button>

                <modal-less-ribbon-button
                        :not-available="hide_selection_controls"
                        :selected_file="selected_file"
                        icon="floor.png"
                        option_name="As parquet"
                        @on-btn-clicked="download_as_parquet"
                ></modal-less-ribbon-button>

                <modal-less-ribbon-button
                        :not-available="hide_selection_controls"
                        :selected_file="selected_file"
                        icon="key-chain.png"
                        option_name="S3 Keys"
                        @on-btn-clicked="download_s3_keys"
                ></modal-less-ribbon-button>
            </div>

            <span class="ribbon-title">Import/Export</span>
            <div class="ribbon-section">
                <span class="section-title">Import</span>
                <small-ribbon-button
                        :not-available="true"
                        option_name="Import File"
                        :selected_file="selected_file"
                        icon="import.png"
                ></small-ribbon-button>

                <small-ribbon-button
                        :not-available="true"
                        option_name="Import From Archive"
                        :selected_file="selected_file"
                        icon="archive.png"
                ></small-ribbon-button>
            </div>
            <div class="ribbon-section">
                <span class="section-title">Advanced</span>
                <apply-python-script-ribbon-button
                        :not-available="hide_selection_controls"
                        :selected_file="selected_file"
                        icon="python.png"
                ></apply-python-script-ribbon-button>

                <modal-less-ribbon-button
                        :not-available="false"
                        :selected_file="selected_file"
                        icon="file_1.png"
                        option_name="Script Store"
                        @on-btn-clicked="this.$router.push('/script-store')"
                ></modal-less-ribbon-button>
            </div>


        </div>

        <div class="ribbon-tab" id="client-tab">
            <span class="ribbon-title">Tasks</span>
            <div class="ribbon-section">
                <span class="section-title"></span>
                <ribbon-button
                        :not-available="true"
                        option_name="Deploy"
                        :selected_file="selected_file"
                        icon="deployment.png"
                ></ribbon-button>

                <ribbon-button
                        :not-available="true"
                        option_name="Synchronize"
                        :selected_file="selected_file"
                        icon="synchronization.png"
                ></ribbon-button>
            </div>
        </div>


        <div class="ribbon-static">
            <span id="selected_files"></span>
            <br>
            <br>
            Last Update
            <br>
            <span>{{last_updated}}</span>

        </div>
    </div>

</template>

<script>
    import $ from 'jquery';

    import DetailsRibbonButton from "./ribbon_buttons/DetailsRibbonButton";
    import PreviewRibbonButton from "./ribbon_buttons/PreviewRibbonButton";
    import S3KeyRibbonButton from "./ribbon_buttons/S3KeyRibbonButton";
    import AccessLogRibbonButton from "./ribbon_buttons/AccessLogRibbonButton";
    import RibbonButton from "./ribbon_buttons/RibbonButton";
    import ColumnsRibbonButton from "./ribbon_buttons/ColumnsRibbonButton";
    import ExtractColumnsRibbonButton from "./ribbon_buttons/ExtractColumnsRibbonButton";
    import Add2BookmarksRibbonButton from "./ribbon_buttons/Add2BookmarksRibbonButton";
    import FilterByTypeRibbonButton from "./ribbon_buttons/FilterByTypeRibbonButton";
    import FilterBySizeRibbonButton from "./ribbon_buttons/FilterBySizeRibbonButton";
    import FilterBydATERibbonButton from "./ribbon_buttons/FilterByDateRibbonButton";
    import AllBookmarksRibbonButton from "./ribbon_buttons/AllBookmarksRibbonButton";
    import SmallRibbonButton from "./ribbon_buttons/SmallRibbonButton";
    import ModalLessRibbonButton from "./ribbon_buttons/ModalLessRibbonButton";
    import ApplyPythonScriptRibbonButton from "./ribbon_buttons/ApplyPythonScriptRibbonButton";

    export default {
        name: "RibbonPanel",
        props: [
            "last_updated", "selected_files"
        ],
        data() {
            return {
                selected_file : {},
                hide_file_controls : true,
                hide_selection_controls : true
            };
        },

        watch:{
            selected_files(new_val) {

                var selected_files_count = new_val.length;
                if(selected_files_count === 0){
                    // hide selections controls
                    this.hide_file_controls = true
                    this.hide_selection_controls = true;
                }else{
                    if(selected_files_count === 1){
                        this.hide_file_controls = false;
                        this.hide_selection_controls = false;
                        this.selected_file = new_val[0];
                    }else{
                        this.hide_selection_controls = false;
                        this.selected_file = new_val;
                    }
                }
            }
        },
        created() {
            //const this_ = this;
            $(function () {
                (function ($) {
                    $.fn.ribbon = function (id) {
                        if (!id) {
                            if (this.attr('id')) {
                                id = this.attr('id');
                            }
                        }

                        var that = function () {
                            return thatRet;
                        };

                        var thatRet = that;

                        that.selectedTabIndex = -1;

                        var tabNames = [];

                        that.goToBackstage = function () {
                            ribObj.addClass('backstage');
                        }

                        that.returnFromBackstage = function () {
                            ribObj.removeClass('backstage');
                        }
                        var ribObj = null;

                        that.init = function (id) {
                            if (!id) {
                                id = 'ribbon';
                            }

                            ribObj = $('#' + id);
                            ribObj.find('.ribbon-window-title').after('<div id="ribbon-tab-header-strip"></div>');
                            var header = ribObj.find('#ribbon-tab-header-strip');

                            ribObj.find('.ribbon-tab').each(function (index) {
                                var id = $(this).attr('id');
                                if (id == undefined || id == null) {
                                    $(this).attr('id', 'tab-' + index);
                                    id = 'tab-' + index;
                                }
                                tabNames[index] = id;

                                var title = $(this).find('.ribbon-title');
                                var isBackstage = $(this).hasClass('file');
                                header.append('<div id="ribbon-tab-header-' + index + '" class="ribbon-tab-header"></div>');
                                var thisTabHeader = header.find('#ribbon-tab-header-' + index);
                                thisTabHeader.append(title);
                                if (isBackstage) {
                                    thisTabHeader.addClass('file');

                                    thisTabHeader.click(function () {
                                        that.switchToTabByIndex(index);
                                        that.goToBackstage();
                                    });
                                } else {
                                    if (that.selectedTabIndex == -1) {
                                        that.selectedTabIndex = index;
                                        thisTabHeader.addClass('sel');
                                    }

                                    thisTabHeader.click(function () {
                                        that.returnFromBackstage();
                                        that.switchToTabByIndex(index);
                                    });
                                }
                                $(this).hide();
                            });

                            ribObj.find('.ribbon-button').each(function () {
                                var title = $(this).find('.button-title');
                                title.detach();
                                $(this).append(title);

                                var el = $(this);

                                this.enable = function () {
                                    el.removeClass('disabled');
                                };

                                this.disable = function () {
                                    el.addClass('disabled');
                                };

                                this.isEnabled = function () {
                                    return !el.hasClass('disabled');
                                };

                                if ($(this).find('.ribbon-hot').length == 0) {
                                    $(this).find('.ribbon-normal').addClass('ribbon-hot');
                                }
                                ;

                                if ($(this).find('.ribbon-disabled').length == 0) {
                                    $(this).find('.ribbon-normal').addClass('ribbon-disabled');
                                    $(this).find('.ribbon-normal').addClass('ribbon-implicit-disabled');
                                }
                                ;

                            });

                            ribObj.find('.ribbon-section').each(function () {
                                $(this).after('<div class="ribbon-section-sep"></div>');
                            });

                            ribObj.find('div').attr('unselectable', 'on');
                            ribObj.find('span').attr('unselectable', 'on');
                            ribObj.attr('unselectable', 'on');

                            that.switchToTabByIndex(that.selectedTabIndex);
                        }

                        that.switchToTabByIndex = function (index) {
                            var headerStrip = $('#ribbon #ribbon-tab-header-strip');
                            headerStrip.find('.ribbon-tab-header').removeClass('sel');
                            headerStrip.find('#ribbon-tab-header-' + index).addClass('sel');

                            $('#ribbon .ribbon-tab').hide();
                            $('#ribbon #' + tabNames[index]).show();
                        }

                        $.fn.enable = function () {
                            if (this.hasClass('ribbon-button')) {
                                if (this[0] && this[0].enable) {
                                    this[0].enable();
                                }
                            } else {
                                this.find('.ribbon-button').each(function () {
                                    $(this).enable();
                                });
                            }
                        }

                        $.fn.disable = function () {
                            if (this.hasClass('ribbon-button')) {
                                if (this[0] && this[0].disable) {
                                    this[0].disable();
                                }
                            } else {
                                this.find('.ribbon-button').each(function () {
                                    $(this).disable();
                                });
                            }
                        }

                        $.fn.isEnabled = function () {
                            if (this[0] && this[0].isEnabled) {
                                return this[0].isEnabled();
                            } else {
                                return true;
                            }
                        }


                        that.init(id);

                        $.fn.ribbon = that;
                    };

                })($);

                $(document).ready(function () {
                    $('#ribbon').ribbon();

                    $('#enable-btn').click(function () {
                        $('#del-table-btn').enable();
                        $('#del-page-btn').enable();
                        $('#save-btn').enable();
                        $('#other-btn-2').enable();

                        $('#enable-btn').hide();
                        $('#disable-btn').show();
                    });
                    $('#disable-btn').click(function () {
                        $('#del-table-btn').disable();
                        $('#del-page-btn').disable();
                        $('#save-btn').disable();
                        $('#other-btn-2').disable();

                        $('#disable-btn').hide();
                        $('#enable-btn').show();
                    });

                });
            });
        },
        methods: {
            refresh_clicked(){
                this.$emit('on-refresh')
            },
            filter_by_bookmarks(n){
                this.$emit('on-filter-by-bookmarks',n)
            },
            filter_by_date(n){
                this.$emit('on-filter-by-date',n)
            },
            filter_by_type(n){
                this.$emit('on-filter-by-type',n)
            },
            filter_by_size(n){
                this.$emit('on-filter-by-size',n)
            },
            download_s3_keys() {
                const ls = this.s3_keys_from_selection();
                const blob = new Blob([ls.join("\n")], {type: 'application/txt'})
                this.download_content(blob, 'keys.txt')
            },

            download_as_parquet() {
                const ls = this.s3_keys_from_selection();
                const blob = new Blob([ls.join("\n")], {type: 'application/txt'})
                this.download_content(blob, 'archive.parquet.zip')
            },

            download_as_csv() {
                const ls = this.s3_keys_from_selection();
                const blob = new Blob([ls.join("\n")], {type: 'application/txt'})
                this.download_content(blob, 'archive.csv.zip')
            },

            download_as_xlsx() {
                const ls = this.s3_keys_from_selection();
                const blob = new Blob([ls.join("\n")], {type: 'application/txt'})
                this.download_content(blob, 'archive.xlsx.zip')
            },

            download_raw() {
                const ls = this.s3_keys_from_selection();

                this.$axios
                    .post('http://127.0.0.1:5000/download-files', {
                        mode: "raw",
                        keys: ls
                    })
                    .then(response => {
                        console.log(response);
                    })

                //const blob = new Blob([ls.join("\n")], { type: 'application/txt' })
                //this.download_content(blob,'archive.raw.zip')
            },

            download_content(content, filename) {
                alert(filename)
                const link = document.createElement('a')
                link.href = URL.createObjectURL(content)
                link.download = filename
                link.click()
                URL.revokeObjectURL(link.href)
            },

            s3_keys_from_selection() {
                var ls = []
                for (let x in this.selected_files) {
                    if (!this.selected_files[x].folder) {
                        ls.push(this.selected_files[x].title)
                    }
                }
                return ls;
            }
        },
        components: {
            ApplyPythonScriptRibbonButton,
            ModalLessRibbonButton,
            SmallRibbonButton,
            AllBookmarksRibbonButton,
            FilterBydATERibbonButton,
            FilterBySizeRibbonButton,
            FilterByTypeRibbonButton,
            Add2BookmarksRibbonButton,
            ExtractColumnsRibbonButton,
            ColumnsRibbonButton,
            RibbonButton,
            AccessLogRibbonButton,
            S3KeyRibbonButton,
            PreviewRibbonButton,
            DetailsRibbonButton
        },
    }
</script>

<style type="text/css">
    .ui-menu {
        width: 100px;
        font-size: 63%;
        z-index: 3; /* over ext-wide titles */
    }

    *, *:before, *:after {
        -moz-box-sizing: border-box;
        -webkit-box-sizing: border-box;
        box-sizing: border-box;
    }

    html, body.flexbox-body {
        height: 100%;
        padding: 0;
        margin: 0;
    }

    .page-container {
        /* background: rgba(255, 255, 255, .1); */
        padding: 10px;
    }

    .flexbox-parent {
        width: 100%;
        height: 100%;

        display: flex;
        flex-direction: column;

        justify-content: flex-start; /* align items in Main Axis */
        align-items: stretch; /* align items in Cross Axis */
        align-content: stretch; /* Extra space in Cross Axis */
    }

    .flexbox-item {
        padding: 8px;
    }

    .flexbox-item-grow {
        flex: 1; /* same as flex: 1 1 auto; */
    }

    /* .flexbox-item.header {
        background: rgba(255, 0, 0, .1);
    }
    .flexbox-item.footer {
        background: rgba(0, 255, 0, .1);
    }
    .flexbox-item.content {
        background: rgba(0, 0, 255, .1);
    } */
    .fill-area {
        display: flex;
        flex-direction: row;

        justify-content: flex-start; /* align items in Main Axis */
        align-items: stretch; /* align items in Cross Axis */
        align-content: stretch; /* Extra space in Cross Axis */

    }

    .fill-area-content {
        background: rgba(0, 0, 0, .3);
        border: 1px solid #000000;

        /* Needed for when the area gets squished too far and there is content that can't be displayed */
        overflow: auto;
    }

    header, footer {
        /* flex: 0 0; */
        background-color: #f7f7f7;
        /* padding: 1rem; */
    }

    /* custom alignment (set by 'renderColumns' event) */
    table.fancytree-ext-table {
        /* flex: 1; */
        width: 100%;
        border-collapse: collapse;
        border: 1px dotted #f4f4f8;
        caption-side: bottom;
    }

    /* Support scrolling  */
    div.fancytree-grid-container {
        /* Use whole parent heigt*/
        flex: 1;
        /* Stretch embedded table */
        display: flex;
        flex-direction: column;
        min-height: 30px;
        /*  */
        padding: 0;
        border: 1px solid gray;
        /* The div should not be stretched by the content rows, because we want to
           adust the row count from div height instead: */
        overflow-y: hidden;

        position: relative;
        padding-right: 16px;
    }

    div.fancytree-grid-container > table.fancytree-ext-grid {
        flex: 1;
        width: 100%;
        border: 0;
        margin: 1px 0 1px 0; /* 1px above and below. */
    }

    /* Ext-grid breaks if another extension hides rows. */
    table.fancytree-ext-grid tbody tr.fancytree-hide {
        display: table-row;
    }

    /* Set alternating row colors (define BEFORE standard css). */
    table.fancytree-ext-table tbody tr:nth-child(even) {
        background-color: #fafafa;
    }

    table.fancytree-ext-table thead th.parent-path {
        text-align: left;
    }

    table.fancytree-ext-table td:nth-child(2) {
        width: 50px;
    }

    table.fancytree-ext-table td:nth-child(4) {
        text-align: right;
    }

    table.fancytree-ext-table td:nth-child(5) {
        text-align: center;
    }

    /* PlainScrollbar-specific Styles */
    .plain-scrollbar[data-scrollable="false"] {
        visibility: hidden;
    }


    @media screen and (max-width: 768px) {
        .ribbon-static {
            display: none !important;
        }
    }

    .page {
        border: 1px solid #a5acb5;
        margin: 20px;
        padding: 15px;
        -webkit-box-shadow: #000000 0px 0px 10px;
        -moz-box-shadow: #000000 0px 0px 10px;
        box-shadow: #000000 0px 0px 10px;
        background: #FFF;
    }

    .ribbon-static {
        display: block;
        float: right;
        text-align: center;
        font-size: 12px;
        margin-right: 40px;
        margin-top: -100px;
    }

    #ribbon {
        font-family: "Segoe UI", Verdana, Tahoma, Helvetica, sans-serif;
        cursor: default;
        font-size: 8pt;
        padding-top: 0px;
        background-color: #eaedf1;
        border-bottom: 1px solid #8b9097;
        -webkit-box-shadow: #8b9097 0px 1px 3px;
        -moz-box-shadow: #8b9097 0px 1px 3px;
        box-shadow: #8b9097 0px 1px 3px;
        overflow: overlay;
        z-index: 25;
        top: 0;
        left: 0;
        right: 0;
        height: 160px;
        min-width: 768px;
    }

    #ribbon.backstage {
        height: auto;
        bottom: 0;
    }

    #ribbon .ribbon-window-title {

    }

    #ribbon #ribbon-tab-header-strip {
        margin: 20px 0 0 10px;
        white-space: nowrap;
    }

    #ribbon .ribbon-tab-header {
        display: inline;
        margin: 0 5px;
        padding: 5px 10px;
        font-size: 8pt;
        color: #444; /*border: 1px solid #eaedf1;*/
        border-bottom: 0px solid #fff;
        -webkit-border-radius: 4px 4px 0px 0px;
        -moz-border-radius: 4px 4px 0px 0px;
        border-radius: 4px 4px 0px 0px;
        position: relative;
        z-index: 40;
    }

    #ribbon.backstage .ribbon-tab-header {
        border-bottom: 1px solid #1f48a1;
    }

    #ribbon .ribbon-tab-header:hover {
        background: #f1f3f4;
        border: 1px solid #b6babf;
        margin: -1px 4px;
        cursor: pointer;
    }

    #ribbon.backstage .ribbon-tab-header {
        border-bottom: 1px solid #1f48a1;
    }

    #ribbon .ribbon-tab-header.sel, #ribbon .ribbon-tab-header.sel:hover {
        background: #fff;
        margin: -1px 4px;
        border: 1px solid #b6babf;
        border-bottom: 1px solid #fff;
        cursor: default;
        z-index: 45;
    }

    #ribbon .ribbon-tab-header.file {
        padding: 5px 20px;
        background: #2860b3;
        background: -webkit-gradient(linear, 0 0, 0 bottom, from(#4488e5), to(#2860b3));
        background: -moz-linear-gradient(#4488e5, #2860b3);
        -pie-background: linear-gradient(#4488e5, #2860b3);
        border: 1px solid #1f48a1;
        margin: -1px 4px;
        border-bottom: 1px solid #4488e5;
        cursor: default;
        color: #fff;
    }


    #ribbon .ribbon-tab-header.file:hover {
        background: #3870c3;
        background: -webkit-gradient(linear, 0 0, 0 bottom, from(#5498f5), to(#3870c3));
        background: -moz-linear-gradient(#5498f5, #3870c3);
        -pie-background: linear-gradient(#5498f5, #3870c3);
        border: 1px solid #1f48a1;
        cursor: pointer;
        border-bottom: 1px solid #4488e5;
        z-index: 55;
        position: relative;
    }

    #ribbon .ribbon-tab-header.file.sel {
        background: #4488e5;
        background: -webkit-gradient(linear, 0 0, 0 bottom, from(#2860b3), to(#4488e5));
        background: -moz-linear-gradient(#2860b3, #4488e5);
        -pie-background: linear-gradient(#2860b3, #4488e5);
        border: 1px solid #1f48a1;
        cursor: pointer;
        border-bottom: 1px solid #4488e5;
        z-index: 55;
        position: relative;
    }

    #ribbon .ribbon-tab {
        height: 120px;
        padding: 5px;
        margin-top: 5px;
        border-top: 0px solid #b6babf;
        background: #FFF repeat-x bottom;
        background: -webkit-gradient(linear, 0 0, 0 bottom, from(#ffffff), to(#eaedf1));
        background: -moz-linear-gradient(#ffffff, #eaedf1); /*-pie-background: linear-gradient(#ffffff, #eaedf1);*/
        overflow: hidden;
        min-width: 500px;
        z-index: 30;
        -pie-watch-ancestors: 2;
    }

    #ribbon .ribbon-tab.file {
        padding: 0;
        margin-top: 5px;
        border-top: 1px solid #1f48a1;

        background-color: #4488e5;
        filter: progid:DXImageTransform.Microsoft.gradient(GradientType=1, startColorstr=#4488e5, endColorstr=#ffffff);
        background-image: -moz-linear-gradient(left, #4488e5 15%, #ffffff 100%);
        background-image: -webkit-linear-gradient(left, #4488e5 15%, #ffffff 100%);
        background-image: -ms-linear-gradient(left, #4488e5 15%, #ffffff 100%);
        background-image: linear-gradient(left, #4488e5 15%, #ffffff 100%);
        background-image: -o-linear-gradient(left, #4488e5 15%, #ffffff 100%);
        background-image: -webkit-gradient(linear, left bottom, right bottom, color-stop(15%, #4488e5), color-stop(100%, #ffffff));


        overflow: hidden;
        min-width: 500px;
        z-index: 30;
    }

    #ribbon .ribbon-backstage {
        display: none;
    }


    #ribbon.backstage .ribbon-backstage {
        display: block;
        position: absolute;
        top: 60px;
        left: 0;
        right: 0;
        bottom: 0;
        padding: 10px;
        background-color: #FFF;
    }

    #ribbon .section-title {
        color: #5B626C;
        text-align: center;
        clear: left;
        display: block;
        position: absolute;
        bottom: -12px;
        left: 0;
        right: 0;

    }

    #ribbon .ribbon-section {
        float: left;
        position: relative;
        height: 82px;
    }

    #ribbon .ribbon-section-sep {
        border-left: 1px solid #E0E0E0;
        border-right: 1px solid #fff;
        margin: 0 5px;
        height: 75px;
        position: relative;
        width: 0;
        float: left;
    }

    #ribbon .ribbon-button {
        padding: 4px 6px;
        border: 1px solid transparent;
        -webkit-border-radius: 3px 3px 3px 3px;
        -moz-border-radius: 3px 3px 3px 3px;
        border-radius: 3px 3px 3px 3px;

    }

    #ribbon .ribbon-button-large {
        text-align: center;
        height: 75px;
        min-width: 44px;
        float: left;
    }

    #ribbon .ribbon-button-small {
        height: 25px;
        padding: 3px 4px;
        text-align: left;

    }

    #ribbon .ribbon-button .button-help {
        display: none;
    }

    #ribbon .ribbon-button .button-title {
        color: #444;
    }

    #ribbon .ribbon-button-large .button-title {
        clear: left;
        display: block;
    }

    #ribbon .ribbon-button-large .ribbon-icon {
        margin: auto;
    }

    #ribbon .ribbon-button-small .ribbon-icon {
        width: 16px;
        height: 16px;
        float: left;
        clear: left;
        margin: -1px 5px 0px 1px;
    }

    #ribbon .ribbon-button .ribbon-icon.ribbon-hot, #ribbon .ribbon-button .ribbon-icon.ribbon-disabled {
        display: none;
    }

    #ribbon .ribbon-button-large .ribbon-icon.ribbon-normal {
        display: block;
    }

    #ribbon .ribbon-button:hover .ribbon-icon.ribbon-normal {
        display: none;
    }

    #ribbon .ribbon-button-large:hover .ribbon-icon.ribbon-hot {
        display: block;
    }

    #ribbon .ribbon-button-small .ribbon-icon.ribbon-normal {
        display: inline;
    }

    #ribbon .ribbon-button-small:hover .ribbon-icon.ribbon-hot {
        display: inline;
    }

    #ribbon .ribbon-button:hover, #ribbon .ribbon-button.sel {
        border: 1px solid #F1C43F;
        background: #fdeeb3;
        cursor: pointer;

    }

    #ribbon .ribbon-button:active {
        border: 1px solid #F1C43F;
        background: #F1C43F;
        cursor: pointer;
    }

    #ribbon .ribbon-button.disabled .ribbon-icon, #ribbon .ribbon-button.disabled:hover .ribbon-icon {
        display: none;
    }

    #ribbon .ribbon-button.disabled .ribbon-icon.ribbon-disabled {
        display: block;
        opacity: 0.8;

    }

    #ribbon .ribbon-button.disabled .ribbon-icon.ribbon-implicit-disabled {
        opacity: 0.4;
    }

    #ribbon .ribbon-button.disabled:hover {
        border: 1px solid transparent;
        background: transparent;
        cursor: default;
    }

    #ribbon .ribbon-button.disabled:active {
        border: 1px solid transparent;
        background: transparent;
        cursor: default;
    }

    #ribbon .ribbon-button.disabled .button-title {
        color: #888;
    }

    .ribbon-tooltip {
        font-family: "Segoe UI", Verdana, Tahoma, Helvetica, sans-serif;
        font-size: 10pt;
        position: fixed;
        z-index: 5000;
        border: 1px solid #8b9097;
        background-color: #e5e5f0;
        background: -webkit-gradient(linear, 0 0, 0 bottom, from(#ffffff), to(#e5e5f0));
        background: -moz-linear-gradient(#ffffff, #e5e5f0);
        -pie-background: linear-gradient(#ffffff, #e5e5f0);
        padding: 5px;
        -webkit-box-shadow: #c6c9cd 1px 1px 3px;
        -moz-box-shadow: #c6c9cd 1px 1px 3px;
        box-shadow: #c6c9cd 1px 1px 3px;
        -webkit-border-radius: 2px 2px 2px 2px;
        -moz-border-radius: 2px 2px 2px 2px;
        border-radius: 2px 2px 2px 2px;
        width: 200px;
        top: 150px !important;
    }


    .file-options {

    }
</style>