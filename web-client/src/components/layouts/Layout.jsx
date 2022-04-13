import React from 'react';
import {Route, Routes} from "react-router-dom";
import Sidebar from "../sidebar/Sidebar";
import BotRouters from "../BotRouters";
import TopNav from "../topnav/TopNav";

import "./layout.css"

const Layout = () => {
	return (
		<Routes>
			<Route path="*" element={
				<div className="layout">
					<Sidebar/>
					<div className="layout__content">
						<TopNav/>
						<div className="layout__content-main">
							<BotRouters/>
						</div>
					</div>
				</div>
			}/>
		</Routes>
	);
};

export default Layout;