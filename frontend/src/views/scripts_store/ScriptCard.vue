<template>
    <div class="card">
        <div class="card-header pb-0 px-3">
            <h6 class="mb-0">{{ title }}</h6>
        </div>
        <div class="card-body pt-4 p-3">
            <ul class="list-group">
                <li
                        v-for="({ name, developer, description }, index) of bills"
                        :key="index"
                        class="list-group-item border-0 d-flex p-4 mb-2 bg-gray-100 border-radius-lg"
                >
                    <div class="d-flex flex-column">
                        <h6 class="mb-3 text-sm">{{ name }}</h6>
                        <span class="mb-2 text-xs">
              Developer Name:
              <span class="text-dark font-weight-bold ms-sm-2">
                {{ developer }}</span
              >
            </span>
                        <span class="mb-2 text-xs">
              Description:
              <span class="text-dark ms-sm-2 font-weight-bold">
                {{ description }}</span
              >
            </span>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
    export default {
        name: "ScriptCard",
        props: {
            title: {
                type: String,
                default: "",
            },
            bills: {
                type: Array,
                name: String,
                developer: String,
                description: String,
                default: () => [],
            },
        }
    };
</script>
