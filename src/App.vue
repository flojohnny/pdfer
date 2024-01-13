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
        :allResults="allResults"
        :activeResults="activeResults"
        :benchedResults="benchedResults"
        @add-pages="activateResults"
        @remove-pages="benchResults"
      ></list-view>
      <pdf-view class="pdf-view" v-if="Object.keys(activeResults).length > 0 && showPdf"></pdf-view>
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
      allResults: {},
      activeResults: {},
      benchedResults: {},
      showPdf: false,
    };
  },
  components: {
    ListView,
    PdfView,
  },
  mounted() {
    this.updatePDF(this.activeResults);
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
      this.allResults = data.matches;
      this.benchedResults = data.matches;
    },

    async updatePDF(pages) {
      this.showPdf = false;
      const response = await fetch("http://localhost:5000/api/update_pdf", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(pages),
      });

      await response.json();
      this.showPdf = true;
    },

    activateResults(pages) {
      // add pages to active results
      for (const page of pages) {
        const pdf = page.pdf;
        if (pdf in this.activeResults) {
          this.activeResults[pdf].push(page);
        } else {
          this.activeResults[pdf] = [page];
        }
      }
      this.activeResults = { ...this.activeResults };

      // remove pages from benched results
      for (let i = pages.length - 1; i >= 0; i--) {
        const page = pages[i];
        const pdf = page.pdf;
        if (pdf in this.benchedResults) {
          const index = this.benchedResults[pdf].indexOf(page);
          if (index > -1) {
            this.benchedResults[pdf].splice(index, 1);
            if (this.benchedResults[pdf].length === 0) {
              delete this.benchedResults[pdf];
            }
          }
        }
      }

      this.benchedResults = { ...this.benchedResults };

      // update PDF
      this.updatePDF(this.activeResults);
    },

    benchResults(pages) {
      // add pages to benched results
      for (const page of pages) {
        const pdf = page.pdf;
        if (pdf in this.benchedResults) {
          this.benchedResults[pdf].push(page);
        } else {
          this.benchedResults[pdf] = [page];
        }
      }
      this.benchedResults = { ...this.benchedResults };

      // remove pages from active results
      for (let i = pages.length - 1; i >= 0; i--) {
        const page = pages[i];
        const pdf = page.pdf;
        if (pdf in this.activeResults) {
          const index = this.activeResults[pdf].indexOf(page);
          if (index > -1) {
            this.activeResults[pdf].splice(index, 1);
            if (this.activeResults[pdf].length === 0) {
              delete this.activeResults[pdf];
            }
          }
        }
      }

      this.activeResults = { ...this.activeResults };

      // update PDF
      this.updatePDF(this.activeResults);
    },

    clearSelection() {
      this.activeResults = { ...{} };
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

  justify-content: space-between;
  align-items: top;
  padding: 20px;
  background-color: #444;
  color: #fff;
  height: 100vh;
  overflow: hidden;
}

.list-view {
  width: 50%;
}

.pdf-view {
  height: 100%;
  width: 50%;
}

.list-view {
  float: left;
}
</style>
