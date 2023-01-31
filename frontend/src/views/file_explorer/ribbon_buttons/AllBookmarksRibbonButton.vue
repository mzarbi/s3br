<template>
    <general-ribbon-button
            v-bind="$props"
            option_name="All Bookmarks"
            :dialog_title="dialog_title_"
            @on-confirm-clicked="confirm_clicked"
            @on-cancel-clicked="cancel_clicked"
            @on-modal-opened="get_all_bookmarks"
    >
        <table class="customers">
            <tr v-for="(bookmark, index) in bookmarks" :key="index">
                <td style="width:50%">{{ bookmark.name }}</td>
                <td style="width:50%"><input type="checkbox" v-model="bookmark.selected"></td>
            </tr>
        </table>
    </general-ribbon-button>
</template>

<script>
    import GeneralRibbonButton from "./GeneralRibbonButton";
    export default {
        name: "AllBookmarksRibbonButton",
        props: {
            notAvailable: Boolean,
            icon: String,
            option_name: String,
            dialog_title: String
        },
        data(){
            return {
                bookmarks: []
            }
        },
        methods: {
            get_all_bookmarks(){
                const this_ = this;
                this.$axios
                    .get(this.$store.state.api_url + 'bookmark-group')
                    .then(response => {
                        this_.bookmarks = []
                        for(let x in response.data.bookmarks_list){
                            this_.bookmarks.push({
                                name : response.data.bookmarks_list[x],
                                selected : false
                            })
                        }
                    })
            },
            confirm_clicked(){
                const this_ = this;
                const xx = []
                for(let x in this_.bookmarks){
                    if(this_.bookmarks[x].selected){
                        xx.push(this_.bookmarks[x])
                    }
                }
                this.$axios
                    .post(this.$store.state.api_url + 'bookmark-group-keys',{
                        list : xx
                    }).then(response => {
                        this.$emit('on-btn-clicked',response.data.bookmarks_keys);
                    })
            },
            cancel_clicked(){

            }
        },
        computed: {
            dialog_title_() {
                return "All Bookmarks";
            }
        },
        components: {GeneralRibbonButton}
    }
</script>

<style scoped>
    .customers {
        font-family: Arial, Helvetica, sans-serif;
        border-collapse: collapse;
        width: 100%;
    }

    .customers td, #customers th {
        border: 1px solid #ddd;
        padding: 8px;
    }

    .customers tr:nth-child(even){background-color: #f2f2f2;}

    .customers tr:hover {background-color: #ddd;}

    .customers th {
        padding-top: 12px;
        padding-bottom: 12px;
        text-align: left;
        background-color: #04AA6D;
        color: white;
    }
</style>