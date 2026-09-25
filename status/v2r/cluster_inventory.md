# V2R cluster inventory

2026-09-25T09:56:32.965834+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318837145600 available bytes; 82.21% used; 112480393 free inodes.

server1 `/home`: 318837145600 available bytes; 82.21% used; 112480393 free inodes.

server1 `/tmp`: 318837145600 available bytes; 82.21% used; 112480393 free inodes.

server1 `/var/tmp`: 318837145600 available bytes; 82.21% used; 112480393 free inodes.

server1 `/mnt/raid5`: 357277859840 available bytes; 98.36% used; 337556887 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22827220992 available bytes; 98.73% used; 110410482 free inodes.

server2 `/home`: 22827220992 available bytes; 98.73% used; 110410482 free inodes.

server2 `/tmp`: 22827220992 available bytes; 98.73% used; 110410482 free inodes.

server2 `/var/tmp`: 22827220992 available bytes; 98.73% used; 110410482 free inodes.

server2 `/mnt/raid5`: 317182586880 available bytes; 97.81% used; 445091606 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84421734400 available bytes; 95.29% used; 114156039 free inodes.

server3 `/home`: 84421734400 available bytes; 95.29% used; 114156039 free inodes.

server3 `/data`: 142293688320 available bytes; 98.03% used; 225810193 free inodes.

server3 `/tmp`: 84421734400 available bytes; 95.29% used; 114156039 free inodes.

server3 `/var/tmp`: 84421734400 available bytes; 95.29% used; 114156039 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105614508032 available bytes; 94.11% used; 114350275 free inodes.

server4 `/home`: 105614508032 available bytes; 94.11% used; 114350275 free inodes.

server4 `/data`: 240030064640 available bytes; 96.68% used; 224992196 free inodes.

server4 `/tmp`: 105614508032 available bytes; 94.11% used; 114350275 free inodes.

server4 `/var/tmp`: 105614508032 available bytes; 94.11% used; 114350275 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
