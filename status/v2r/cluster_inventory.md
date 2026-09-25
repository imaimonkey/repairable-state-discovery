# V2R cluster inventory

2026-09-25T02:46:48.864420+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318959640576 available bytes; 82.21% used; 112480441 free inodes.

server1 `/home`: 318959640576 available bytes; 82.21% used; 112480441 free inodes.

server1 `/tmp`: 318959640576 available bytes; 82.21% used; 112480441 free inodes.

server1 `/var/tmp`: 318959640576 available bytes; 82.21% used; 112480441 free inodes.

server1 `/mnt/raid5`: 416181538816 available bytes; 98.09% used; 337603986 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 23006208000 available bytes; 98.72% used; 110410439 free inodes.

server2 `/home`: 23006208000 available bytes; 98.72% used; 110410439 free inodes.

server2 `/tmp`: 23006208000 available bytes; 98.72% used; 110410439 free inodes.

server2 `/var/tmp`: 23006208000 available bytes; 98.72% used; 110410439 free inodes.

server2 `/mnt/raid5`: 482599337984 available bytes; 96.67% used; 445113105 free inodes.
| server3 | True | ['3'] | [] | reference_compatible=True |

server3 `/`: 84350099456 available bytes; 95.29% used; 114156089 free inodes.

server3 `/home`: 84350099456 available bytes; 95.29% used; 114156089 free inodes.

server3 `/data`: 145257705472 available bytes; 97.99% used; 225810931 free inodes.

server3 `/tmp`: 84350099456 available bytes; 95.29% used; 114156089 free inodes.

server3 `/var/tmp`: 84350099456 available bytes; 95.29% used; 114156089 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 101969219584 available bytes; 94.31% used; 114350980 free inodes.

server4 `/home`: 101969219584 available bytes; 94.31% used; 114350980 free inodes.

server4 `/data`: 3928866816 available bytes; 99.95% used; 224968784 free inodes.

server4 `/tmp`: 101969219584 available bytes; 94.31% used; 114350980 free inodes.

server4 `/var/tmp`: 101969219584 available bytes; 94.31% used; 114350980 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
