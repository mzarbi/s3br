<template>
    <single-file-ribbon-button
            v-bind="$props"
            option_name="Set Label"
            :dialog_title="dialog_title_"
            @on-confirm-clicked="confirm_clicked"
            @on-cancel-clicked="cancel_clicked"
    >
        <div class="input-group mb-3">
            <input type="text" class="form-control" aria-label="Recipient's username"
                   aria-describedby="basic-addon2"
                   style="height: 2rem;line-height: 0;"
            >
        </div>
    </single-file-ribbon-button>
</template>

<script>
    import SingleFileRibbonButton from "./SingleFileRibbonButton";

    export default {
        name: "SetLabelRibbonButton",
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
                return "File : " + this.selected_file.title;
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