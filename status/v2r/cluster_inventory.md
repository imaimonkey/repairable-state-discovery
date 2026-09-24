# V2R cluster inventory

2026-09-24T11:13:29.781409+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324366376960 available bytes; 81.90% used; 112488956 free inodes.

server1 `/home`: 324366376960 available bytes; 81.90% used; 112488956 free inodes.

server1 `/tmp`: 324366376960 available bytes; 81.90% used; 112488956 free inodes.

server1 `/var/tmp`: 324366376960 available bytes; 81.90% used; 112488956 free inodes.

server1 `/mnt/raid5`: 469705203712 available bytes; 97.85% used; 337691365 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 57680723968 available bytes; 96.78% used; 110430162 free inodes.

server2 `/home`: 57680723968 available bytes; 96.78% used; 110430162 free inodes.

server2 `/tmp`: 57680723968 available bytes; 96.78% used; 110430162 free inodes.

server2 `/var/tmp`: 57680723968 available bytes; 96.78% used; 110430162 free inodes.

server2 `/mnt/raid5`: 511151837184 available bytes; 96.47% used; 445174097 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85762375680 available bytes; 95.21% used; 114198697 free inodes.

server3 `/home`: 85762375680 available bytes; 95.21% used; 114198697 free inodes.

server3 `/data`: 163927941120 available bytes; 97.73% used; 225816969 free inodes.

server3 `/tmp`: 85762375680 available bytes; 95.21% used; 114198697 free inodes.

server3 `/var/tmp`: 85762375680 available bytes; 95.21% used; 114198697 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105731928064 available bytes; 94.10% used; 114348900 free inodes.

server4 `/home`: 105731928064 available bytes; 94.10% used; 114348900 free inodes.

server4 `/data`: 115700613120 available bytes; 98.40% used; 225258151 free inodes.

server4 `/tmp`: 105731928064 available bytes; 94.10% used; 114348900 free inodes.

server4 `/var/tmp`: 105731928064 available bytes; 94.10% used; 114348900 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
