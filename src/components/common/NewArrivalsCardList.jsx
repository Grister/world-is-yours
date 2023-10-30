import React, { useState } from "react";
import Card from "./Card";
import cardData from "../../data";
import ArrowRight from '../../assets/icons/dark/icon-arrow-right.svg'

const NewArrivalsCardList = () => {
  const initialVisibleCards = 7;
  const [visibleCards, setVisibleCards] = useState(initialVisibleCards);

  const loadMoreCards = () => {
    setVisibleCards(
      (prevVisibleCards) => prevVisibleCards + initialVisibleCards
    );
  };

  return (
    <div>
      <h1 className="flex items-center justify-center mt-20 mb-10 font-raleway text-custom-black text-30px">
        Новинки
      </h1>
      <div className="flex flex-wrap justify-around mb-20 ml-3 mr-3">
        {cardData.slice(0, visibleCards).map((item, index) => (
          <Card data={item} key={index} />
        ))}
        {visibleCards < cardData.length && (
          <div
            className="flex justify-center w-80 m-4 border-2 border-gray-light rounded-lg relative"
            onClick={loadMoreCards}
          >
            <div className="flex flex-col justify-center justify-items-center mb-10">
            <p className="font-inter py-2 px-4 rounded text-custom-black">
              Дивитися ще
            </p>
            <img src={ArrowRight} alt="icon arrow right" className="text-custom-black w-8 ml-12" />
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default NewArrivalsCardList;



