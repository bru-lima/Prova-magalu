sku = "abncve68588958df"
estoque = 0 

db.produto.update_one(
    {"sku": sku},
    {"$inc": {"estoque": estoque}}
)
