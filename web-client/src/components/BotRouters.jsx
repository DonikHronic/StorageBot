import React from 'react';
import {Routes, Route} from "react-router-dom";
import Dashboard from "../pages/Dashboard";
import Customers from "../pages/Customers";

const BotRouters = () => {
	return (
		<Routes>
			<Route path="/" exact element={<Dashboard/>}/>
			<Route path="customers" element={<Customers/>}/>
		</Routes>
	);
};

export default BotRouters;