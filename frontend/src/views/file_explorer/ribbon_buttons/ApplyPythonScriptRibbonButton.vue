
<template>
    <general-ribbon-button
            v-bind="$props"
            option_name="Apply Python Script"
            :dialog_title="dialog_title_"
            @on-confirm-clicked="confirm_clicked"
            @on-cancel-clicked="cancel_clicked"
    >
        <table class="customers">
            <tr>
                <td><input type="radio"></td>
                <td>Decode Gzip</td>
            </tr>
            <tr>
                <td><input type="radio"></td>
                <td>Anonymize Data</td>
            </tr>
        </table>
    </general-ribbon-button>
</template>

<script>
    import GeneralRibbonButton from "./GeneralRibbonButton";
    export default {
        name: "ApplyPythonScriptRibbonButton",
        props: {
            notAvailable: Boolean,
            icon: String,
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
                return "Apply Python Script";
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