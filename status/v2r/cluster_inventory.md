# V2R cluster inventory

2026-09-25T02:48:52.209378+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318959419392 available bytes; 82.21% used; 112480441 free inodes.

server1 `/home`: 318959419392 available bytes; 82.21% used; 112480441 free inodes.

server1 `/tmp`: 318959419392 available bytes; 82.21% used; 112480441 free inodes.

server1 `/var/tmp`: 318959419392 available bytes; 82.21% used; 112480441 free inodes.

server1 `/mnt/raid5`: 416175996928 available bytes; 98.09% used; 337603751 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22999625728 available bytes; 98.72% used; 110410439 free inodes.

server2 `/home`: 22999625728 available bytes; 98.72% used; 110410439 free inodes.

server2 `/tmp`: 22999625728 available bytes; 98.72% used; 110410439 free inodes.

server2 `/var/tmp`: 22999625728 available bytes; 98.72% used; 110410439 free inodes.

server2 `/mnt/raid5`: 482536476672 available bytes; 96.67% used; 445112935 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84351496192 available bytes; 95.29% used; 114156077 free inodes.

server3 `/home`: 84351496192 available bytes; 95.29% used; 114156077 free inodes.

server3 `/data`: 145222361088 available bytes; 97.99% used; 225810897 free inodes.

server3 `/tmp`: 84351496192 available bytes; 95.29% used; 114156077 free inodes.

server3 `/var/tmp`: 84351496192 available bytes; 95.29% used; 114156077 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 101767823360 available bytes; 94.32% used; 114350975 free inodes.

server4 `/home`: 101767823360 available bytes; 94.32% used; 114350975 free inodes.

server4 `/data`: 58924363776 available bytes; 99.19% used; 224968784 free inodes.

server4 `/tmp`: 101767823360 available bytes; 94.32% used; 114350975 free inodes.

server4 `/var/tmp`: 101767823360 available bytes; 94.32% used; 114350975 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
