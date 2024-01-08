const { defineConfig } = require('@vue/cli-service');

module.exports = defineConfig({
  pluginOptions: {
    electronBuilder: {
      nodeIntegration: true
    }
  },
  chainWebpack: (config) => {
    // Add a rule to handle PDF files
    config.module
    .rule('pdf')
    .test(/\.(pdf)(\?.*)?$/)
    .use('file-loader')
    .loader('file-loader')
    .options({
      name: 'assets/[name].[hash:8].[ext]',
    })
    .end();
  },
  transpileDependencies: [
    // add your dependencies here if needed
  ]
});

