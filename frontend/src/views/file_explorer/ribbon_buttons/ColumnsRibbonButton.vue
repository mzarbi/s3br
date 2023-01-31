<template>
    <single-file-ribbon-button
            v-bind="$props"
            option_name="Columns"
            :dialog_title="dialog_title_"
            @on-confirm-clicked="confirm_clicked"
            @on-cancel-clicked="cancel_clicked"
            @on-modal-opened="get_file_columns"
    >
        <table class="customers">
            <tr v-for="(value, index) in file_columns" :key="index">
                <td style="width:50%">{{value.name}}</td>
                <td style="width:50%">{{value.datatype}}</td>
            </tr>
        </table>
    </single-file-ribbon-button>
</template>

<script>
    import SingleFileRibbonButton from "./SingleFileRibbonButton";
    export default {
        name: "ColumnsRibbonButton",
        props: {
            notAvailable: Boolean,
            icon: String,
            selected_file: Object,
            option_name: String,
            dialog_title: String
        },
        data(){
            return {
                file_columns : []
            }
        },
        methods: {
            confirm_clicked(){

            },
            cancel_clicked(){

            },
            get_file_columns(){
                const this_ = this;
                this.$axios
                    .post(this.$store.state.api_url + 'file-columns',{key : this.selected_file.data.s3_key})
                    .then(response => {
                        this_.file_columns = response.data.file_columns;
                    })
            }
        },
        computed: {
            dialog_title_() {
                return "File Columns : " + this.selected_file.title;
            }
        },
        components: {SingleFileRibbonButton}
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