module.exports = {
    productionSourceMap: false,
    chainWebpack: config => {
      config.module
        .rule('raw')
        .test(/\.txt$/)
        .use('raw-loader')
        .loader('raw-loader')
        .end()
    }
};