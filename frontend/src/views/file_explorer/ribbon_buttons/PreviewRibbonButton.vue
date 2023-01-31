<template>
    <single-file-ribbon-button
            v-bind="$props"
            option_name="Preview"
            :dialog_title="dialog_title_"
            @on-confirm-clicked="confirm_clicked"
            @on-cancel-clicked="cancel_clicked"
            @on-modal-opened="get_file_preview"
    >
    <span>{{message}}</span>
    </single-file-ribbon-button>
</template>

<script>
    import SingleFileRibbonButton from "./SingleFileRibbonButton";

    export default {
        name: "PreviewRibbonButton",
        props: {
            notAvailable: Boolean,
            icon: String,
            selected_file: Object,
            option_name: String,
            dialog_title: String
        },
        data(){
            return {
                message : ""
            }
        },
        created() {
        },
        methods: {
            confirm_clicked(){

            },
            cancel_clicked(){

            },
            get_file_preview(){
                const this_ = this;
                this.$axios
                    .post(this.$store.state.api_url + 'file-preview',{key : this.selected_file.data.s3_key})
                    .then(response => {
                        this_.message = response.data.message;
                    })
            }
        },
        computed: {
            dialog_title_() {
                return "File Preview : " + this.selected_file.title;
            }
        },
        components: {SingleFileRibbonButton}
    }
</script>

<style scoped>

</style>