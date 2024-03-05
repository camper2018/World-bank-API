SELECT * FROM World_Bank_Data.topics;
SELECT * FROM World_Bank_Data.sources;
SELECT * FROM World_Bank_Data.indicators;
SELECT * FROM World_Bank_Data.indicator_data;

INSERT INTO World_Bank_Data.countries
(id,iso2code,name,region_id,admin_region_id,income_level_id,lending_type_id,capital_city,longitude,lattitude)
VALUES('ABW','AW','Aruba','LCN','','HIC','LNX','Oranjestad','-70.0167','12.5167');

INSERT INTO World_Bank_Data.regions
(id, iso2code, value)
VALUES('NA', 'NA', 'Aggregates');
SELECT * from World_Bank_Data.countries as c inner join World_Bank_Data.income_levels as i 
where c.income_level_id=i.id;
SELECT * from World_Bank_Data.lending_types
 ;
SELECT * from World_Bank_Data.regions;
INSERT INTO World_Bank_Data.regions (id, iso2code, value) 
VALUES('LCN', 'ZJ', 'Latin America & Caribbean');
SELECT * from World_Bank_Data.income_levels;

SELECT * from World_Bank_Data.countries as c inner join World_Bank_Data.regions as r
where c.region_id=r.id;
INSERT INTO World_Bank_Data.admin_regions
(id, iso2code, value) VALUES('LAC', 'XJ', 'Latin America & Caribbean (excluding high income)');
SELECT * from World_Bank_Data.lending_types;

SELECT * from World_Bank_Data.countries as c inner join World_Bank_Data.admin_regions as r
where c.admin_region_id=r.id;
INSERT INTO World_Bank_Data.lending_types
(id,iso2code,value) VALUES('LNX', 'XX', 'Not classified');
SELECT * from World_Bank_Data.countries as c inner join World_Bank_Data.lending_types as l
where c.lending_type_id=l.id;
SELECT * from sources;
INSERT INTO World_Bank_Data.sources
(id, last_updated, name, code, description, url, data_availability,metadata_availability, concepts)
VALUES('1', '2019-10-23', 'Doing Business', 'DBS', '', '', 'Y', 'Y', '3');
SELECT * from indicators;
INSERT INTO World_Bank_Data.indicators
(id, name, unit, source_id, source_note, source_organization) 
VALUES('ENF.CONT.COEN.ATDR', 'Enforcing contracts: Alternative dispute resolution (0-3) (DB16-20 methodology)', '', '1','The alternative dispute resolution evaluates two aspects: (i) whether domestic commercial arbitration is regulated by law, all disputes can be submitted to arbitration and valid arbitration clauses are usually enforced by courts; and (ii) whether voluntary mediation and/or conciliation are a recognized way of resolving commercial disputes, they are regulated by law and there are financial incentives for parties to attempt mediation of conciliation. The index is computed based on the methodology in the DB17-20 studies.', '');
SELECT * FROM  World_Bank_Data.sources AS s INNER JOIN World_Bank_Data.indicators AS i 
WHERE s.id=i.source_id;
SELECT * FROM topics;
SELECT * FROM indicator_topic_union;
INSERT INTO  World_Bank_Data.indicator_topic_union
(topic_id, indicator_id)
VALUES('19', 'ENF.CONT.COEN.ATDR');
DELETE FROM  World_Bank_Data.indicator_topic_union WHERE id=2;
SELECT t.* , i.*, s.* FROM topics AS t
JOIN indicator_topic_union AS itu ON t.id=itu.topic_id
JOIN indicators AS i ON i.id = itu.indicator_id
JOIN sources AS s ON s.id= i.source_id;
SELECT * FROM indicator_data;
INSERT INTO World_Bank_Data.indicator_data 
(indicator_id, country_name, country_iso2, country_iso3, date, value, unit, obs_status,decimal_val)
VALUES('ENF.CONT.COEN.ATDR','Aruba', 'AW', 'ARB', '2007', 62.148998260498,'', '', 0);
SELECT * FROM indicator_data;


