<template>
    <div class="py-4 container-fluid">

        <div class="chat" v-for="notification in notifications" :key="notification.id">
            <img class="chat_avatar" src="../assets/img/notifications/download.png">
            <div class="chat_info">
                <div class="contact_name">{{ notification.message}}</div>
                <div class="contact_msg"></div>
            </div>
            <div class="chat_status">
                <div class="chat_date">{{format_date(notification.time)}}</div>
            </div>
        </div>

    </div>
</template>

<script>

    import moment from "moment";

    export default {
        name: "notifications",
        data(){
            return {
                notifications : []
            }
        },
        created() {
            const this_ = this;
            this.$axios_loaderless
                .post(this_.$store.state.api_url + 'notifications', {page: 5})
                .then(response => {
                    this_.notifications = response.data;
                })
        },
        methods: {
            format_date(dt){
                return moment.unix(dt).fromNow()
            },
        },
    };
</script>
<style>
    img.chat_avatar {
        width: 45px;
        height: 45px;
        border-radius: 7px;
        margin-right: 8px;
    }

    img.chat_avatar {
        width: 45px;
        margin-left: 2rem;
        border-radius: 7px;
    }

    .chat {
        display: flex;
        justify-content: space-between;
        padding: 15px 0px;
        border-bottom: 1px solid #d3d3d35e;
    }

    .chat:hover{
        box-shadow: 1px 6px 18px rgba(31, 37, 72, 0.45);
        cursor: grabbing;
    }

    .contact_name {
        font-weight: 500;

        color: #34394F;
        font-size: 15px;
        margin-bottom: 2px;
    }

    .contact_msg {
        font-size: 12px;
        color: #a5a5a5;
        font-weight: 600;
    }

    .chat_info {
        width: 100%;
    }

    .chat_date {
        font-size: 12px;
        color: #5a5a5a;
        margin-bottom: 2px;
    }

    .chat_new {
        padding: 2px 5px;
        font-size: 11px;
        border-radius: 2px;
    }

    .chat_status {
        width: 15%;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
</style>