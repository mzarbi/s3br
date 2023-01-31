<template>
    <general-ribbon-button
            v-bind="$props"
            option_name="Type"
            :dialog_title="dialog_title_"
            @on-confirm-clicked="confirm_clicked"
            @on-cancel-clicked="cancel_clicked"
    >
        <table class="customers">
            <tr>
                <td>CSV</td>
                <td><input v-model="csv" type="checkbox"></td>
            </tr>
            <tr>
                <td>XLSX</td>
                <td><input v-model="xlsx" type="checkbox"></td>
            </tr>
            <tr>
                <td>Parquet</td>
                <td><input v-model="parquet" type="checkbox"></td>
            </tr>
            <tr>
                <td>TXT</td>
                <td><input v-model="txt" type="checkbox"></td>
            </tr>
            <tr>
                <td>JSON</td>
                <td><input v-model="json" type="checkbox"></td>
            </tr>
        </table>
    </general-ribbon-button>
</template>

<script>
    import GeneralRibbonButton from "./GeneralRibbonButton";
    export default {
        name: "FilterByTypeRibbonButton",
        props: {
            notAvailable: Boolean,
            icon: String,
            option_name: String,
            dialog_title: String
        },
        data(){
            return {
                csv : false,
                xlsx : false,
                parquet : false,
                txt : false,
                json : false
            }
        },
        methods: {
            confirm_clicked(){
                this.$emit('on-btn-clicked',{
                    csv : this.csv,
                    xlsx : this.xlsx,
                    parquet : this.parquet,
                    txt : this.txt,
                    json : this.json
                })
            },
            cancel_clicked(){

            }
        },
        computed: {
            dialog_title_() {
                return "Filter By Type";
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