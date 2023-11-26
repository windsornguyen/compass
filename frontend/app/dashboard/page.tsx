'use client';

import { useEffect, useState } from 'react';

import { rectSortingStrategy } from '@dnd-kit/sortable';

import Footer from '../../components/Footer';
import Navbar from '../../components/Navbar';
import useAuthStore from '../../store/authSlice';
import UserState from '../../store/userSlice';

import { Canvas } from './Canvas';

const Dashboard: React.FC = () => {
  const [isLoading, setIsLoading] = useState(true);
  const { user, isAuthenticated, checkAuthentication } = useAuthStore((state) => state);
  const userProfile = UserState((state) => state.profile);
  useEffect(() => {
    checkAuthentication()
      .then(() => setIsLoading(false))
      .catch((error) => {
        console.error('Auth error:', error);
        setIsLoading(false);
      });
  }, [checkAuthentication]);

  useEffect(() => {
    if (!isLoading && !isAuthenticated) {
      window.location.href = `${process.env.BACKEND}/login`;
    }
  }, [isAuthenticated, isLoading]);

  // const handleDragEnd = (event: DragEndEvent) => {
  //   // Logic for handling drag end event (update Zustand store)
  //   // ...
  // };

  return (
    <>
      <Navbar />
      <div className='flex flex-col h-screen pt-20 p-2 rounded-xl'>
        <main className='flex p-2 flex-grow bg-[#FAFAFA] rounded-xl shadow-xl'>
          {user && (
            <Canvas
              user={userProfile}
              trashable
              columns={2}
              strategy={rectSortingStrategy}
              wrapperStyle={() => ({
                width: 150,
                height: 150,
              })}
            />
          )}
        </main>
        <Footer />
      </div>
    </>
  );
};

export default Dashboard;
