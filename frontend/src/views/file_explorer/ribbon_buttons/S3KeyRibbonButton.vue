<template>
    <single-file-ribbon-button
            v-bind="$props"
            option_name="S3 Key"
            :dialog_title="dialog_title_"
            @on-confirm-clicked="confirm_clicked"
            @on-cancel-clicked="cancel_clicked"
            @on-modal-opened="resolve_s3_key"
    >
        <div class="input-group mb-3">
            <input type="text" class="form-control" aria-label="Recipient's username"
                   aria-describedby="basic-addon2" v-model="s3key"
                   style="height: 2rem;line-height: 0;"
                   :readonly="true"
            >
            <div class="input-group-append">
                <button class="btn btn-outline-secondary"
                        style="height: 2rem;line-height: 0;"
                        type="button"
                        @click="clipboardClick"
                >Copy To Clipboard</button>
            </div>
        </div>
    </single-file-ribbon-button>
</template>

<script>
    import SingleFileRibbonButton from "./SingleFileRibbonButton";

    function copyToClipboard(value) {
        const textArea = document.createElement('textarea')
        textArea.textContent = value
        document.body.append(textArea)
        textArea.select()
        document.execCommand('copy')
    }
    export default {
        name: "S3KeyRibbonButton",
        props: {
            notAvailable: Boolean,
            icon: String,
            selected_file: Object,
            option_name: String,
            dialog_title: String
        },
        data(){
            return {
                s3key : ""
            }
        },
        methods: {
            confirm_clicked(){

            },
            cancel_clicked(){

            },
            clipboardClick(){
                copyToClipboard(this.selected_file.data.s3_key);
            },
            resolve_s3_key(){
                this.s3key = this.selected_file.data.s3_key;
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