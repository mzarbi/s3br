<template>
    <single-file-ribbon-button
            v-bind="$props"
            option_name="Add To Bookmarks List"
            :dialog_title="dialog_title_"
            @on-confirm-clicked="confirm_clicked"
            @on-cancel-clicked="cancel_clicked"
            @on-modal-opened="get_bookmarks_list"
    >

        <span>Please select or create new group</span>
        <div class="input-group mb-3">

            <select v-model="group_selected"
                    style="height: 2rem; line-height: 0; border-radius: 0.5rem 0px 0px 0.5rem; border: 1px solid #d2d6da;">
                <option disabled value="">Please select one</option>
                <option>New Group</option>
                <option v-for="(value, index) in bookmarks_list" :key="index">{{ value }}</option>
            </select>
            <input type="text" class="form-control"
                   style="height: 2rem;line-height: 0;margin-left:5px"
                   v-model="group_chosen"
                   :disabled="group_input_disabled"
            >
        </div>
        <span>Set Label</span>
        <div class="input-group mb-3">
            <input type="text" class="form-control"
                   style="height: 2rem;line-height: 0;"
                   v-model="label_chosen"
            >
        </div>
    </single-file-ribbon-button>
</template>

<script>
    import SingleFileRibbonButton from "./SingleFileRibbonButton";

    export default {
        name: "Add2BookmarksRibbonButton",
        props: {
            notAvailable: Boolean,
            icon: String,
            selected_file: Object,
            option_name: String,
            dialog_title: String
        },
        data() {
            return {
                group_selected: "New Group",
                group_chosen: "",
                group_input_disabled: false,
                label_chosen: this.selected_file.title,
                bookmarks_list: []
            }
        },

        watch: {
            group_selected(new_val) {
                if (new_val == "New Group") {
                    this.group_input_disabled = false;
                    this.group_chosen = "";
                } else {
                    this.group_input_disabled = true;
                    this.group_chosen = this.group_selected;
                }
            }
        },
        methods: {
            get_bookmarks_list() {
                const this_ = this;
                this_.label_chosen = this.selected_file.title;
                this_.$axios
                    .get(this.$store.state.api_url + 'bookmark-group')
                    .then(response => {
                        this_.bookmarks_list = response.data.bookmarks_list;
                    })
            },
            confirm_clicked() {
                const this_ = this;
                if (this.label_chosen == "" || this.group_chosen == "") {
                    this_.$swal.fire({
                        icon: 'error',
                        title: 'Could not perform this task',
                        text: 'Please verify your inputs',
                    });
                } else {
                    this_.$axios
                        .post(this.$store.state.api_url + 'add-to-bookmarks', {
                            key: this.selected_file.data.s3_key,
                            label: this.label_chosen,
                            group: this.group_chosen
                        })
                        .then(response => {
                            console.log(response)
                        })
                }
            },
            cancel_clicked() {

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

    .customers tr:nth-child(even) {
        background-color: #f2f2f2;
    }

    .customers tr:hover {
        background-color: #ddd;
    }

    .customers th {
        padding-top: 12px;
        padding-bottom: 12px;
        text-align: left;
        background-color: #04AA6D;
        color: white;
    }
</style>