<template>
  <ul class="main-list">
    <ul
      class="sub-list"
      v-for="[item, subItems] in Object.entries(items)"
      :key="item"
    >
      <li class="list-object">
        <h1 class="list-title">{{ item }}</h1>
        <div>
          <button
            v-if="type === 'unselected'"
            class="add-btn"
            @click="addAction(items[item])"
          ></button>
          <button
            v-if="type === 'selected'"
            class="remove-btn"
            @click="removeAction(items[item])"
          ></button>
        </div>
      </li>

      <li class="sub-object" v-for="subItem in subItems" :key="subItem.page">
        <h1 class="sub-title">{{ subItem.page }}</h1>
        <div>
          <button
            v-if="type === 'unselected'"
            class="add-btn"
            @click="addAction([subItem])"
          ></button>
          <button
            v-if="type === 'selected'"
            class="remove-btn"
            @click="removeAction([subItem])"
          ></button>
        </div>
      </li>
    </ul>
  </ul>
</template>

<script>
export default {
  props: {
    items: {
      type: Object,
      required: true,
    },
    type: {
      type: String,
      required: true,
    },
  },
  watch: {
    items() {
      this.localItems = this.items;
      console.log(this.type, "changed", JSON.stringify(this.items));
    },
  },
  methods: {
    addAction(item) {
      this.$emit("add", item);
    },
    removeAction(item) {
      this.$emit("remove", item);
    },
  },
};
</script>

<style scoped>
.list-object,
.sub-object {
  height: fit-content;
  cursor: pointer;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  border: 1px solid rgba(144, 144, 144, 0.393);
  border-radius: 5px;
  box-shadow: 1px 1px 3px rgba(83, 83, 83, 0.445);
  background: #444;
  margin: 5px;
}

.list-object .list-title,
.sub-object .sub-title {
  width: 75%;
  word-wrap: break-word;
}

.add-btn {
  width: 20px;
  height: 20px;
  border-radius: 10px;
  border: none;
  cursor: pointer;
  margin: 0 5px;
}

.add-btn:hover {
  background: #1ab553;
}

.remove-btn {
  width: 20px;
  height: 20px;
  border-radius: 10px;
  border: none;
  cursor: pointer;
  margin: 0 5px;
}

.remove-btn:hover {
  background: #b51a1a;
}
</style>
