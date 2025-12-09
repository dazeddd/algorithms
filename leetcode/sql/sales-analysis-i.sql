
with aggregate_sale as (
    select seller_id, sum(price) total_sales
        from Sales
    group by seller_id
), ranking as (
    select seller_id, rank() over (order by total_sales desc) sale_rank from aggregate_sale
) select seller_id from ranking where sale_rank=1;
