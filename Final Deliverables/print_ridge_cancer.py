print('Ridge Model Tested on Unseen Data')
ridge = Ridge(alpha=best_alpha)
ridge.fit(Xtrain_cancer[~arr_cancer],ytrain_cancer[~arr_cancer])
ypred = ridge.predict(Xtest_cancer)
print('Score on holdout data: {:.4f}'.format(r2_score(ytest_cancer,ypred)))