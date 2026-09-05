(function(){
  const colours=[
    ['Black / White','https://cdn.shopify.com/s/files/1/2185/2813/files/W54341R_06401_b1_s1_a1_m209_2954e25a-00d0-4434-a3d0-edfd73ac4f88_750x.jpg?v=1770668709'],
    ['Navy / White','https://cdn.shopify.com/s/files/1/2185/2813/files/W54341R_04893_b2_s1_a1_dFA26_m277_750x.jpg?v=1786395609'],
    ['White / Black','https://cdn.shopify.com/s/files/1/2185/2813/files/W54341R_0001_b1_s1_a6_dSP26_m246_750x.jpg?v=1773825379'],
    ['Anthracite / White','https://cdn.shopify.com/s/files/1/2185/2813/files/W54341R_06640_b1_s1_a7_m161_750x.jpg?v=1765174633'],
    ['Grass','https://cdn.shopify.com/s/files/1/2185/2813/files/W54341R_08023_b1_s1_a1_dSU26_m246_1_750x.jpg?v=1784543081'],
    ['California Blue','https://cdn.shopify.com/s/files/1/2185/2813/files/W54341R_08305_b1_s1_a3_dFA26_m191_750x.jpg?v=1785918892'],
    ['Pink','https://cdn.shopify.com/s/files/1/2185/2813/files/W54341R_0998_b1_s1_a8_m261_750x.jpg?v=1775683801']
  ];
  const sizes=['XXS','XS','S','M','L','XL','2XL'];
  const variants=[];
  colours.forEach(([colour,image])=>sizes.forEach(top=>sizes.forEach(bottom=>variants.push({sku:`AIR-${colour.replace(/\W/g,'').toUpperCase()}-${top}-${bottom}`,options:[{name:'Colour',value:colour},{name:'Top Size',value:top},{name:'Bottom Size',value:bottom}],price:26,compareAt:95,image,available:true}))));
  window.STORE_PRODUCTS.unshift({handle:'airbrush-set',title:'Airbrush Set',vendor:'Alo Yoga',type:'Sportswear/Sets/',tags:['collection:new','collection:sets','category:tops','category:bottoms','airbrush','alo-yoga'],description:'<p>A complete two-piece Airbrush set with a sculpting sports bra and coordinating high-waist bottom. Choose the size of each piece separately for your perfect fit.</p>',images:colours.map(x=>x[1]),variants,options:['Colour','Top Size','Bottom Size'],price:26,compareAt:95,colour:'7 colours',collections:['new','sets','tops','bottoms','airbrush'],aggregate:true,gift:{title:'Alo Yoga Tote Bag',image:'https://www.summersnkrs.com/cdn/shop/files/image_17_60bccbf9-b2ce-4883-8edf-33439f942542.jpg?v=1749202203'},colourData:colours});
})();
