# V2R cluster inventory

2026-09-25T21:00:55.369637+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318699089920 available bytes; 82.22% used; 112476322 free inodes.

server1 `/home`: 318699089920 available bytes; 82.22% used; 112476322 free inodes.

server1 `/tmp`: 318699089920 available bytes; 82.22% used; 112476322 free inodes.

server1 `/var/tmp`: 318699089920 available bytes; 82.22% used; 112476322 free inodes.

server1 `/mnt/raid5`: 368615563264 available bytes; 98.31% used; 337539518 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22891540480 available bytes; 98.72% used; 110405678 free inodes.

server2 `/home`: 22891540480 available bytes; 98.72% used; 110405678 free inodes.

server2 `/tmp`: 22891540480 available bytes; 98.72% used; 110405678 free inodes.

server2 `/var/tmp`: 22891540480 available bytes; 98.72% used; 110405678 free inodes.

server2 `/mnt/raid5`: 302374928384 available bytes; 97.91% used; 445055735 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84367843328 available bytes; 95.29% used; 114152624 free inodes.

server3 `/home`: 84367843328 available bytes; 95.29% used; 114152624 free inodes.

server3 `/data`: 126050283520 available bytes; 98.26% used; 225807505 free inodes.

server3 `/tmp`: 84367843328 available bytes; 95.29% used; 114152624 free inodes.

server3 `/var/tmp`: 84367843328 available bytes; 95.29% used; 114152624 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105655033856 available bytes; 94.10% used; 114349517 free inodes.

server4 `/home`: 105655033856 available bytes; 94.10% used; 114349517 free inodes.

server4 `/data`: 226324516864 available bytes; 96.87% used; 224926044 free inodes.

server4 `/tmp`: 105655033856 available bytes; 94.10% used; 114349517 free inodes.

server4 `/var/tmp`: 105655033856 available bytes; 94.10% used; 114349517 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
