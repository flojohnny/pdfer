<template>
  <div id="app">
    <h1>{{ message }}</h1>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: "",
    };
  },
  mounted() {
  },
  methods: {

  }
};
</script>

<style>
body {
  font-family: "Arial", sans-serif;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  background-color: #222;
  color: #fff;
}

#app {
  max-width: 600px;
  margin: 20px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  background-color: #333;
}

#query {
  width: 100%;
  margin-bottom: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 20px, 10px, 20px, 10px;
  background-color: #444;
  color: #fff;
}

#list-component {
  margin-bottom: 20px;
}

.listview {
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: #444;
}

#list {
  list-style-type:none;
  padding: 0;
  margin: 0;
}

li {
  padding: 10px;
  border-bottom: 1px solid #ddd;
  cursor: pointer;
  color: #fff;
  transition: background-color 0.3s;
  user-select: none;
  opacity: 1;
}

li:hover {
  background-color: #3f889c;
}

#pdf-container {
  width: 100%;
  height: 500px; /* Set your preferred height */
  border: 1px solid #ddd;
  border-radius: 4px;
  overflow: hidden;
  background-color: #444;
}

#pdf-container embed {
  width: 100%;
  height: 100%;
}
</style>
