# V2R cluster inventory

2026-09-24T11:15:05.335908+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324358234112 available bytes; 81.91% used; 112488947 free inodes.

server1 `/home`: 324358234112 available bytes; 81.91% used; 112488947 free inodes.

server1 `/tmp`: 324358234112 available bytes; 81.91% used; 112488947 free inodes.

server1 `/var/tmp`: 324358234112 available bytes; 81.91% used; 112488947 free inodes.

server1 `/mnt/raid5`: 466976329728 available bytes; 97.86% used; 337691147 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 57679269888 available bytes; 96.78% used; 110430146 free inodes.

server2 `/home`: 57679269888 available bytes; 96.78% used; 110430146 free inodes.

server2 `/tmp`: 57679269888 available bytes; 96.78% used; 110430146 free inodes.

server2 `/var/tmp`: 57679269888 available bytes; 96.78% used; 110430146 free inodes.

server2 `/mnt/raid5`: 511108169728 available bytes; 96.47% used; 445173929 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85760712704 available bytes; 95.21% used; 114198681 free inodes.

server3 `/home`: 85760712704 available bytes; 95.21% used; 114198681 free inodes.

server3 `/data`: 163913932800 available bytes; 97.73% used; 225816937 free inodes.

server3 `/tmp`: 85760712704 available bytes; 95.21% used; 114198681 free inodes.

server3 `/var/tmp`: 85760712704 available bytes; 95.21% used; 114198681 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105731624960 available bytes; 94.10% used; 114348890 free inodes.

server4 `/home`: 105731624960 available bytes; 94.10% used; 114348890 free inodes.

server4 `/data`: 115696459776 available bytes; 98.40% used; 225258145 free inodes.

server4 `/tmp`: 105731624960 available bytes; 94.10% used; 114348890 free inodes.

server4 `/var/tmp`: 105731624960 available bytes; 94.10% used; 114348890 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
