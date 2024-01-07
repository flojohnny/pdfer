<template>
  <div id="app">
    <div class="search-container">
      <input
        id="query"
        class="usr-input"
        type="text"
        placeholder="Search..."
        v-model="query"
        tabindex="0"
      />
      <button class="usr-btn" @click="updateQuery(query)" tabindex="0">
        Search
      </button>
    </div>
    <div class="results-container">
      <list-view
        class="list-view"
        :matches="results"
        :selection="selection"
        @add-page="addPageToSelection"
        @remove-page="removePageFromSelection"
      ></list-view>
      <pdf-view></pdf-view>
    </div>
  </div>
</template>

<script>
import ListView from "./components/ListView.vue";
import PdfView from "./components/PdfView.vue";

export default {
  data() {
    return {
      query: "",
      results: {},
      selection: {},
    };
  },
  components: {
    ListView,
    PdfView,
  },
  mounted() {
    // when the app is mounted
  },
  methods: {
    async updateQuery(query) {
      this.clearSelection();
      const newQuery = query;
      const response = await fetch("http://localhost:5000/api/update_query", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ query: newQuery }),
      });

      const data = await response.json();
      this.results = data.matches;
      console.log(JSON.stringify(this.results));
    },

    addPageToSelection(page) {
      const pdf = page.pdf;
      if (pdf in this.selection) {
        this.selection[pdf].push(page);
      } else {
        this.selection[pdf] = [page];
      }

      this.selection = { ...this.selection };
    },

    removePageFromSelection(page) {
      const pdf = page.pdf;
      const index = this.selection[pdf].indexOf(page);
      this.selection[pdf].splice(index, 1);
      if (this.selection[pdf].length === 0) {
        delete this.selection[pdf];
      }

      this.selection = { ...this.selection };
    },

    clearSelection() {
      this.selection = {...{}};
    },

  },
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

.search-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.usr-input {
  width: 80%;
  margin-right: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 10px;
  background-color: #444;
  color: #fff;
}

.usr-btn {
  width: 20%;
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 10px;
  background-color: #444;
  color: #fff;
  cursor: pointer;
}

.usr-btn:hover {
  background-color: #333;
}

.results-container {
  display: flex;
  flex-direction: row;
  align-items: start;
}

.list-view {
  float: left;
}

@media (max-width: 768px) {
  .results-container {
    flex-direction: column;
  }
}
</style>
