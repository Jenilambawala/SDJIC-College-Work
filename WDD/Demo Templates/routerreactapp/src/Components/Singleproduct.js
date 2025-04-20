import React, { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'

export const Singleproduct = () => {

    const { id } = useParams();
    const [data, setData] = useState([]);
    useEffect(() => {
        fetch(`https://fakestoreapi.com/products/${id}`)
            .then(response => {
                return response.json();
            }).then(data => {
                setData(data);
            });
    }, [id]);
    return (
        <React.Fragment>
            <section class="bg-light">
                <div class="container pb-5">
                    <div class="row">
                        <div class="col-lg-5 mt-5">
                            <div class="card mb-3">
                                <img class="card-img img-fluid" src={data.image} alt="Card image cap" id="product-detail" />
                            </div>
                        </div>
                        <div class="col-lg-7 mt-5">
                            <div class="card">
                                <div class="card-body">
                                    <h1 class="h2">{data.title}</h1>
                                    <p class="h3 py-2">${data.price}</p>
                                    <p class="py-2">
                                        <i class="fa fa-star text-warning"></i>
                                        <i class="fa fa-star text-warning"></i>
                                        <i class="fa fa-star text-warning"></i>
                                        <i class="fa fa-star text-warning"></i>
                                        <i class="fa fa-star text-secondary"></i>
                                        <span class="list-inline-item text-dark">Rating {data.rate} </span>
                                    </p>
                                    <ul class="list-inline">
                                        <li class="list-inline-item">
                                            <h6>category:</h6>
                                        </li>
                                        <li class="list-inline-item">
                                            <p class="text-muted"><strong>{data.category}</strong></p>
                                        </li>
                                    </ul>

                                    <h6>Description:</h6>
                                    <p> {data.description} </p>
                                    
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </React.Fragment>
    )
}
