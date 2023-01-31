
<template>
    <div class="ribbon-button"
         id="file-details-btn"

         :class="[{disabled : notAvailable},btn_cls]"
    >
        <span class="button-title" @click="openModal">{{option_name}}</span>
        <span class="button-help">This button will add a table to your document.</span>
        <img class="ribbon-icon ribbon-normal" :src="mIconURL" @click="run"/>
        <img class="ribbon-icon ribbon-hot" :src="mIconURL" @click="run"/>
        <img class="ribbon-icon ribbon-disabled" :src="mIconURL" @click="run"/>
    </div>

</template>

<script>
    import {VueFinalModal, ModalsContainer } from 'vue-final-modal'

    export default {
        name: "ModalLessRibbonButton",
        props: {
            notAvailable: Boolean,
            icon: String,
            option_name: String,
            btn_cls: {
                type: String,
                default: "ribbon-button-large"
            },
        },
        data(){
            return {
            }
        },
        computed: {
            mIconURL() {
                return require(`../../../assets/img/ribbon/${this.icon}`);
            },
        },

        methods:{
            run(){
                this.$emit('on-btn-clicked')
            }
        },
        components: [VueFinalModal, ModalsContainer]
    }
</script>

<style scoped>
    ::v-deep .modal-container {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    ::v-deep .modal-content {
        position: relative;
        display: flex;
        flex-direction: column;
        margin: 0 1rem;
        padding: 1rem;
        border: 1px solid #e2e8f0;
        border-radius: 0.25rem;
        background: #fff;
        width: 500px;
    }
    .modal__title {
        margin: 0 2rem 0 0;
        font-size: 1.5rem;
        font-weight: 700;
    }
    .modal__action {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-shrink: 0;
        padding: 1rem 0 0;
    }
    .modal__close {
        position: absolute;
        top: 0.5rem;
        right: 0.5rem;
    }
</style>

<style scoped>
    .dark-mode div::v-deep .modal-content {
        border-color: #2d3748;
        background-color: #1a202c;
    }
</style>