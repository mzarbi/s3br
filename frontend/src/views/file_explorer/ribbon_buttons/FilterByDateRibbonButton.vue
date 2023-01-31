<template>
    <general-ribbon-button
            v-bind="$props"
            option_name="Date"
            :dialog_title="dialog_title_"
            @on-confirm-clicked="confirm_clicked"
            @on-cancel-clicked="cancel_clicked"
    >
        <table class="customers">
            <tr>
                <td><input type="checkbox" v-model="before"></td>
                <td>Last Modified Prior To</td>
                <td><input type="date" v-model="before_value"></td>
            </tr>
            <tr>
                <td><input type="checkbox" v-model="after"></td>
                <td>Last Modified After</td>
                <td><input type="date" v-model="after_value"></td>
            </tr>
        </table>
    </general-ribbon-button>
</template>

<script>
    import GeneralRibbonButton from "./GeneralRibbonButton";
    import moment from "moment";
    export default {
        name: "FilterBydATERibbonButton",
        props: {
            notAvailable: Boolean,
            icon: String,
            option_name: String,
            dialog_title: String
        },
        data(){
            return {
                before : false,
                after : false,
                before_value : moment(new Date()).format('YYYY-MM-DD'),
                after_value : moment(new Date()).format('YYYY-MM-DD'),
            }
        },
        methods: {
            confirm_clicked(){
                this.$emit('on-btn-clicked',{
                    before : this.before,
                    after : this.after,
                    before_value : this.before_value,
                    after_value : this.after_value
                })
            },
            cancel_clicked(){

            }
        },
        computed: {
            dialog_title_() {
                return "Filter By Date";
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