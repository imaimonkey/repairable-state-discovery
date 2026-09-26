# V2R cluster inventory

2026-09-26T08:42:26.971948+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318746869760 available bytes; 82.22% used; 112475802 free inodes.

server1 `/home`: 318746869760 available bytes; 82.22% used; 112475802 free inodes.

server1 `/tmp`: 318746869760 available bytes; 82.22% used; 112475802 free inodes.

server1 `/var/tmp`: 318746869760 available bytes; 82.22% used; 112475802 free inodes.

server1 `/mnt/raid5`: 219080298496 available bytes; 99.00% used; 337538889 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22313336832 available bytes; 98.76% used; 110403903 free inodes.

server2 `/home`: 22313336832 available bytes; 98.76% used; 110403903 free inodes.

server2 `/tmp`: 22313336832 available bytes; 98.76% used; 110403903 free inodes.

server2 `/var/tmp`: 22313336832 available bytes; 98.76% used; 110403903 free inodes.

server2 `/mnt/raid5`: 255348789248 available bytes; 98.24% used; 445024191 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82678448128 available bytes; 95.39% used; 114110809 free inodes.

server3 `/home`: 82678448128 available bytes; 95.39% used; 114110809 free inodes.

server3 `/data`: 123903471616 available bytes; 98.29% used; 225828603 free inodes.

server3 `/tmp`: 82678448128 available bytes; 95.39% used; 114110809 free inodes.

server3 `/var/tmp`: 82678448128 available bytes; 95.39% used; 114110809 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106063745024 available bytes; 94.08% used; 114348137 free inodes.

server4 `/home`: 106063745024 available bytes; 94.08% used; 114348137 free inodes.

server4 `/data`: 89360687104 available bytes; 98.76% used; 224883411 free inodes.

server4 `/tmp`: 106063745024 available bytes; 94.08% used; 114348137 free inodes.

server4 `/var/tmp`: 106063745024 available bytes; 94.08% used; 114348137 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
