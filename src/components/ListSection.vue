<template>
    <ul class="main-list">
      <ul class="sub-list" v-for="[item, subItems] in Object.entries(items)" :key="item">
        <li class="list-object">
          <h1 class="list-title">{{ item }}</h1>
          <div>
            <button class="action-btn" @click="addAction(item)"></button>
          </div>
        </li>
  
        <li class="sub-object" v-for="subItem in subItems" :key="subItem.page" @click="viewAction(subItem)">
          <h1 class="sub-title">{{ subItem.page }}</h1>
          <div>
            <button class="action-btn" @click="addAction(subItem)"></button>
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
    },
  
    methods: {
      addAction(item) {
        this.$emit("add", item);
      },
      removeAction(item) {
        this.$emit("remove", item);
      },
      viewAction(item) {
        this.$emit("view", item);
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
  
  .action-btn {
    width: 20px;
    height: 20px;
    border-radius: 10px;
    border: none;
    cursor: pointer;
    margin: 0 5px;
  }
  
  .action-btn:hover {
    /* Add your hover styles here */
  }
  </style>
  