<template>
    <div class="ribbon-button ribbon-button-large"
         id="file-details-btn"
         :class="{disabled : notAvailable}"
    >
        <span class="button-title" @click="openModal">{{option_name}}</span>
        <span class="button-help">This button will add a table to your document.</span>
        <img class="ribbon-icon ribbon-normal" :src="mIconURL" @click="openModal"/>
        <img class="ribbon-icon ribbon-hot" :src="mIconURL" @click="openModal"/>
        <img class="ribbon-icon ribbon-disabled" :src="mIconURL" @click="openModal"/>

        <vue-final-modal
                v-model="showModal"
                classes="modal-container"
                content-class="modal-content"
                :prevent-click="true"
                :hide-overlay="true"
        >
            <span class="modal__title">File Details</span>
            <div class="modal__content">
                <p>Vue Final Modal is a rend</p>
            </div>

            <div class="modal__action">
                <button class="btn btn-success btn-sm" @click="onConfirm" style="margin: 10px;">confirm</button>
                <button class="btn btn-error btn-sm" @click="onCancel" style="margin: 10px;">cancel</button>
            </div>
        </vue-final-modal>
    </div>

</template>

<script>
    import {VueFinalModal, ModalsContainer } from 'vue-final-modal'

    export default {
        name: "RibbonButton",
        props: {
            notAvailable: Boolean,
            icon: String,
            selected_file: Object,
            option_name: String,
        },
        data(){
            return {
                file_: this.selected_file,
                showModal: false
            }
        },
        computed: {
            mIconURL() {
                return require(`../../../assets/img/ribbon/${this.icon}`);
            }
        },
        methods:{
            openModal(){
                this.showModal = true;
            },
            onConfirm(){
                this.showModal = false;
                alert(this.selected_file);
            },
            onCancel(){
                this.showModal = false;
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