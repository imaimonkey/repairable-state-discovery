# V2R cluster inventory

2026-09-24T11:30:45.494560+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324347850752 available bytes; 81.91% used; 112488851 free inodes.

server1 `/home`: 324347850752 available bytes; 81.91% used; 112488851 free inodes.

server1 `/tmp`: 324347850752 available bytes; 81.91% used; 112488851 free inodes.

server1 `/var/tmp`: 324347850752 available bytes; 81.91% used; 112488851 free inodes.

server1 `/mnt/raid5`: 445437149184 available bytes; 97.96% used; 337689422 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57662984192 available bytes; 96.78% used; 110429995 free inodes.

server2 `/home`: 57662984192 available bytes; 96.78% used; 110429995 free inodes.

server2 `/tmp`: 57662984192 available bytes; 96.78% used; 110429995 free inodes.

server2 `/var/tmp`: 57662984192 available bytes; 96.78% used; 110429995 free inodes.

server2 `/mnt/raid5`: 510609543168 available bytes; 96.47% used; 445173456 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85737967616 available bytes; 95.22% used; 114195952 free inodes.

server3 `/home`: 85737967616 available bytes; 95.22% used; 114195952 free inodes.

server3 `/data`: 163799580672 available bytes; 97.74% used; 225816634 free inodes.

server3 `/tmp`: 85737967616 available bytes; 95.22% used; 114195952 free inodes.

server3 `/var/tmp`: 85737967616 available bytes; 95.22% used; 114195952 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105730891776 available bytes; 94.10% used; 114348877 free inodes.

server4 `/home`: 105730891776 available bytes; 94.10% used; 114348877 free inodes.

server4 `/data`: 115633471488 available bytes; 98.40% used; 225258067 free inodes.

server4 `/tmp`: 105730891776 available bytes; 94.10% used; 114348877 free inodes.

server4 `/var/tmp`: 105730891776 available bytes; 94.10% used; 114348877 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
