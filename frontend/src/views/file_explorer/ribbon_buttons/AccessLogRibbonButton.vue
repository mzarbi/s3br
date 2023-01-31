<template>
    <single-file-ribbon-button
            v-bind="$props"
            option_name="Access Log"
            :dialog_title="dialog_title_"
            @on-confirm-clicked="confirm_clicked"
            @on-cancel-clicked="cancel_clicked"
            @on-modal-opened="get_access_log"
    >
        <table class="customers">
            <tr v-for="(value, index) in access_log" :key="index">
                <td style="width:50%">{{value.name}}</td>
                <td style="width:50%">{{value.date}}</td>
            </tr>
        </table>
    </single-file-ribbon-button>
</template>

<script>
    import SingleFileRibbonButton from "./SingleFileRibbonButton";
    export default {
        name: "AccessLogRibbonButton",
        props: {
            notAvailable: Boolean,
            icon: String,
            selected_file: Object,
            option_name: String,
            dialog_title: String
        },
        data(){
            return {
                access_log : []
            }
        },
        methods: {
            confirm_clicked(){

            },
            cancel_clicked(){

            },
            get_access_log(){
                const this_ = this;
                this.$axios
                    .post(this.$store.state.api_url + 'access-log',{key : this.selected_file.data.s3_key})
                    .then(response => {
                        this_.access_log = response.data.access_log;
                    })
            }
        },
        computed: {
            dialog_title_() {
                return "Access Log : " + this.selected_file.title;
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