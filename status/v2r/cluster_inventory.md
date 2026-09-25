# V2R cluster inventory

2026-09-25T03:02:43.681554+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318942474240 available bytes; 82.21% used; 112480395 free inodes.

server1 `/home`: 318942474240 available bytes; 82.21% used; 112480395 free inodes.

server1 `/tmp`: 318942474240 available bytes; 82.21% used; 112480395 free inodes.

server1 `/var/tmp`: 318942474240 available bytes; 82.21% used; 112480395 free inodes.

server1 `/mnt/raid5`: 416142528512 available bytes; 98.09% used; 337602125 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22997344256 available bytes; 98.72% used; 110410442 free inodes.

server2 `/home`: 22997344256 available bytes; 98.72% used; 110410442 free inodes.

server2 `/tmp`: 22997344256 available bytes; 98.72% used; 110410442 free inodes.

server2 `/var/tmp`: 22997344256 available bytes; 98.72% used; 110410442 free inodes.

server2 `/mnt/raid5`: 466024906752 available bytes; 96.78% used; 445112865 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84345647104 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84345647104 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 144976117760 available bytes; 98.00% used; 225810412 free inodes.

server3 `/tmp`: 84345647104 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84345647104 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105693196288 available bytes; 94.10% used; 114350903 free inodes.

server4 `/home`: 105693196288 available bytes; 94.10% used; 114350903 free inodes.

server4 `/data`: 51869167616 available bytes; 99.28% used; 224967462 free inodes.

server4 `/tmp`: 105693196288 available bytes; 94.10% used; 114350903 free inodes.

server4 `/var/tmp`: 105693196288 available bytes; 94.10% used; 114350903 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
