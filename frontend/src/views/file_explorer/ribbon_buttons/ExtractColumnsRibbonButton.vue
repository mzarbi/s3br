<template>
    <single-file-ribbon-button
            v-bind="$props"
            option_name="Extract Columns"
            :dialog_title="dialog_title_"
            @on-confirm-clicked="confirm_clicked"
            @on-cancel-clicked="cancel_clicked"
    >
        <table class="customers">
            <tr>
                <td>Name</td>
                <td>String</td>
            </tr>
            <tr>
                <td>Size</td>
                <td>Number</td>
            </tr>
            <tr>
                <td>Last Modified</td>
                <td>Date</td>
            </tr>
        </table>
    </single-file-ribbon-button>
</template>

<script>
    import SingleFileRibbonButton from "./SingleFileRibbonButton";
    export default {
        name: "ExtractColumnsRibbonButton",
        props: {
            notAvailable: Boolean,
            icon: String,
            selected_file: Object,
            option_name: String,
            dialog_title: String
        },
        methods: {
            confirm_clicked(){

            },
            cancel_clicked(){

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