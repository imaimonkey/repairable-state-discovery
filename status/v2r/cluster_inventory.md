# V2R cluster inventory

2026-09-24T11:27:38.114325+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324350128128 available bytes; 81.91% used; 112488859 free inodes.

server1 `/home`: 324350128128 available bytes; 81.91% used; 112488859 free inodes.

server1 `/tmp`: 324350128128 available bytes; 81.91% used; 112488859 free inodes.

server1 `/var/tmp`: 324350128128 available bytes; 81.91% used; 112488859 free inodes.

server1 `/mnt/raid5`: 450812960768 available bytes; 97.93% used; 337689825 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 57662676992 available bytes; 96.78% used; 110430024 free inodes.

server2 `/home`: 57662676992 available bytes; 96.78% used; 110430024 free inodes.

server2 `/tmp`: 57662676992 available bytes; 96.78% used; 110430024 free inodes.

server2 `/var/tmp`: 57662676992 available bytes; 96.78% used; 110430024 free inodes.

server2 `/mnt/raid5`: 510728511488 available bytes; 96.47% used; 445173668 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85733597184 available bytes; 95.22% used; 114195821 free inodes.

server3 `/home`: 85733597184 available bytes; 95.22% used; 114195821 free inodes.

server3 `/data`: 163826339840 available bytes; 97.74% used; 225816693 free inodes.

server3 `/tmp`: 85733597184 available bytes; 95.22% used; 114195821 free inodes.

server3 `/var/tmp`: 85733597184 available bytes; 95.22% used; 114195821 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105731014656 available bytes; 94.10% used; 114348877 free inodes.

server4 `/home`: 105731014656 available bytes; 94.10% used; 114348877 free inodes.

server4 `/data`: 115637751808 available bytes; 98.40% used; 225258069 free inodes.

server4 `/tmp`: 105731014656 available bytes; 94.10% used; 114348877 free inodes.

server4 `/var/tmp`: 105731014656 available bytes; 94.10% used; 114348877 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
