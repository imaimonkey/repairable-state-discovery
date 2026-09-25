# V2R cluster inventory

2026-09-25T19:24:36.526055+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318736470016 available bytes; 82.22% used; 112476348 free inodes.

server1 `/home`: 318736470016 available bytes; 82.22% used; 112476348 free inodes.

server1 `/tmp`: 318736470016 available bytes; 82.22% used; 112476348 free inodes.

server1 `/var/tmp`: 318736470016 available bytes; 82.22% used; 112476348 free inodes.

server1 `/mnt/raid5`: 370871382016 available bytes; 98.30% used; 337540816 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23095447552 available bytes; 98.71% used; 110407938 free inodes.

server2 `/home`: 23095447552 available bytes; 98.71% used; 110407938 free inodes.

server2 `/tmp`: 23095447552 available bytes; 98.71% used; 110407938 free inodes.

server2 `/var/tmp`: 23095447552 available bytes; 98.71% used; 110407938 free inodes.

server2 `/mnt/raid5`: 312225660928 available bytes; 97.84% used; 445064420 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84381679616 available bytes; 95.29% used; 114152621 free inodes.

server3 `/home`: 84381679616 available bytes; 95.29% used; 114152621 free inodes.

server3 `/data`: 129281404928 available bytes; 98.21% used; 225808684 free inodes.

server3 `/tmp`: 84381679616 available bytes; 95.29% used; 114152621 free inodes.

server3 `/var/tmp`: 84381679616 available bytes; 95.29% used; 114152621 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105674973184 available bytes; 94.10% used; 114349586 free inodes.

server4 `/home`: 105674973184 available bytes; 94.10% used; 114349586 free inodes.

server4 `/data`: 229636857856 available bytes; 96.83% used; 224930211 free inodes.

server4 `/tmp`: 105674973184 available bytes; 94.10% used; 114349586 free inodes.

server4 `/var/tmp`: 105674973184 available bytes; 94.10% used; 114349586 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
