import React from 'react';
import sidebar_items from '../../assets/JsonData/sidebar_routes.json'
import logo from '../../assets/images/logo.png'
import {Link, useLocation} from "react-router-dom"
import "./sidebar.css"
import SidebarItem from "./SidebarItem";

const Sidebar = () => {
	const location = useLocation();
	const activeItem = sidebar_items.findIndex(item => item.route === location.pathname)
	return (
		<div className="sidebar">
			<div className="sidebar__logo">
				<img src={logo} alt="logo"/>
			</div>
			{
				sidebar_items.map((item, index) => (
					<Link to={item.route} key={index}>
						<SidebarItem
							title={item.display_name}
							icon={item.icon}
							active={index === activeItem}
						/>
					</Link>
				))
			}
		</div>
	);
};

export default Sidebar;