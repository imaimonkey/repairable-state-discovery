# V2R cluster inventory

2026-09-25T09:58:04.795781+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318838091776 available bytes; 82.21% used; 112480393 free inodes.

server1 `/home`: 318838091776 available bytes; 82.21% used; 112480393 free inodes.

server1 `/tmp`: 318838091776 available bytes; 82.21% used; 112480393 free inodes.

server1 `/var/tmp`: 318838091776 available bytes; 82.21% used; 112480393 free inodes.

server1 `/mnt/raid5`: 364745039872 available bytes; 98.33% used; 337557002 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22827782144 available bytes; 98.73% used; 110410485 free inodes.

server2 `/home`: 22827782144 available bytes; 98.73% used; 110410485 free inodes.

server2 `/tmp`: 22827782144 available bytes; 98.73% used; 110410485 free inodes.

server2 `/var/tmp`: 22827782144 available bytes; 98.73% used; 110410485 free inodes.

server2 `/mnt/raid5`: 317140324352 available bytes; 97.81% used; 445091654 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84421091328 available bytes; 95.29% used; 114156039 free inodes.

server3 `/home`: 84421091328 available bytes; 95.29% used; 114156039 free inodes.

server3 `/data`: 142265475072 available bytes; 98.03% used; 225810178 free inodes.

server3 `/tmp`: 84421091328 available bytes; 95.29% used; 114156039 free inodes.

server3 `/var/tmp`: 84421091328 available bytes; 95.29% used; 114156039 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105614467072 available bytes; 94.11% used; 114350276 free inodes.

server4 `/home`: 105614467072 available bytes; 94.11% used; 114350276 free inodes.

server4 `/data`: 240023035904 available bytes; 96.68% used; 224991996 free inodes.

server4 `/tmp`: 105614467072 available bytes; 94.11% used; 114350276 free inodes.

server4 `/var/tmp`: 105614467072 available bytes; 94.11% used; 114350276 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
