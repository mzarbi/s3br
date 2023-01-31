<template>
    <div class="py-4 container-fluid">
        <script-card
                title="Library"
                :bills="script_list"
        />
    </div>
</template>

<script>
    import ScriptCard from "./scripts_store/ScriptCard";

    export default {
        name: "ScriptStore",
        data(){
            return {
                script_list : []
            }
        },
        created() {
            const this_ = this;
            this.$axios
                .get(this.$store.state.api_url + 'script-list')
                .then(response => {
                    this_.script_list = response.data.script_list;
                })
        },
        components : {ScriptCard}
    };
</script>
<style>

</style>