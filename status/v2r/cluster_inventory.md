# V2R cluster inventory

2026-09-25T05:12:07.009656+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318894432256 available bytes; 82.21% used; 112480295 free inodes.

server1 `/home`: 318894432256 available bytes; 82.21% used; 112480295 free inodes.

server1 `/tmp`: 318894432256 available bytes; 82.21% used; 112480295 free inodes.

server1 `/var/tmp`: 318894432256 available bytes; 82.21% used; 112480295 free inodes.

server1 `/mnt/raid5`: 408586924032 available bytes; 98.13% used; 337570554 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22930014208 available bytes; 98.72% used; 110410436 free inodes.

server2 `/home`: 22930014208 available bytes; 98.72% used; 110410436 free inodes.

server2 `/tmp`: 22930014208 available bytes; 98.72% used; 110410436 free inodes.

server2 `/var/tmp`: 22930014208 available bytes; 98.72% used; 110410436 free inodes.

server2 `/mnt/raid5`: 461736968192 available bytes; 96.81% used; 445108819 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84339105792 available bytes; 95.29% used; 114156069 free inodes.

server3 `/home`: 84339105792 available bytes; 95.29% used; 114156069 free inodes.

server3 `/data`: 142792667136 available bytes; 98.03% used; 225815279 free inodes.

server3 `/tmp`: 84339105792 available bytes; 95.29% used; 114156069 free inodes.

server3 `/var/tmp`: 84339105792 available bytes; 95.29% used; 114156069 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105658994688 available bytes; 94.10% used; 114350409 free inodes.

server4 `/home`: 105658994688 available bytes; 94.10% used; 114350409 free inodes.

server4 `/data`: 26321833984 available bytes; 99.64% used; 224960507 free inodes.

server4 `/tmp`: 105658994688 available bytes; 94.10% used; 114350409 free inodes.

server4 `/var/tmp`: 105658994688 available bytes; 94.10% used; 114350409 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
