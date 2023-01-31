<template>
    <general-ribbon-button
            v-bind="$props"
            option_name="Size"
            :dialog_title="dialog_title_"
            @on-confirm-clicked="confirm_clicked"
            @on-cancel-clicked="cancel_clicked"
    >
        <table class="customers">
            <tr>
                <td><input type="checkbox" v-model="lesser"></td>
                <td>Lesser Than</td>
                <td><input type="range" min="0" max="1000" v-model="lesser_value"></td>
                <td>{{ lesser_value }} Mb</td>
            </tr>
            <tr>
                <td><input type="checkbox" v-model="bigger"></td>
                <td>Bigger Than</td>
                <td><input type="range" min="0" max="1000" v-model="bigger_value"></td>
                <td>{{ bigger_value }} Mb</td>
            </tr>
        </table>
    </general-ribbon-button>
</template>

<script>
    import GeneralRibbonButton from "./GeneralRibbonButton";
    export default {
        name: "FilterBySizeRibbonButton",
        props: {
            notAvailable: Boolean,
            icon: String,
            option_name: String,
            dialog_title: String
        },
        data(){
            return {
                lesser : false,
                bigger : false,
                lesser_value : 0,
                bigger_value : 0,
            }
        },
        methods: {
            confirm_clicked(){
                this.$emit('on-btn-clicked',{
                    lesser : this.lesser,
                    bigger : this.bigger,
                    lesser_value : this.lesser_value,
                    bigger_value : this.bigger_value
                })
            },
            cancel_clicked(){

            }
        },
        computed: {
            dialog_title_() {
                return "Filter By Size";
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