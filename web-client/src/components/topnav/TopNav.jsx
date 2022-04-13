import React from 'react';
import "./topnav.css"
import Dropdown from "../dropdown/Dropdown";
import notifications from "../../assets/JsonData/notification.json"
import {Link} from "react-router-dom";

const rendererNotificationItem = (item, index) => (
	<div className="notification-item" key={index}>
		<i className={item.icon}/>
		<span>{item.content}</span>
	</div>
)

const TopNav = () => {
	return (
		<div className="topnav">
			<div className="topnav__search">
				<input type="text" placeholder="Search here..."/>
				<i className="bx bx-search"/>
			</div>
			<div className="topnav__right">
				<div className="topnav__right-item">
					<Dropdown
						icon="bx bx-user"
					/>
				</div>
				<div className="topnav__right-item">
					<Dropdown
						icon="bx bx-bell"
						badge="12"
						contentData={notifications}
						rendererItems={(item, index) => rendererNotificationItem(item, index)}
						rendererFooter={() => <Link to="/">View All</Link>}
					/>
				</div>
				<div className="topnav__right-item">
					<Dropdown/>
				</div>
			</div>
		</div>
	);
};

export default TopNav;