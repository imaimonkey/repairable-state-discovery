# V2R cluster inventory

2026-09-25T20:25:30.697438+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318706089984 available bytes; 82.22% used; 112476327 free inodes.

server1 `/home`: 318706089984 available bytes; 82.22% used; 112476327 free inodes.

server1 `/tmp`: 318706089984 available bytes; 82.22% used; 112476327 free inodes.

server1 `/var/tmp`: 318706089984 available bytes; 82.22% used; 112476327 free inodes.

server1 `/mnt/raid5`: 369625014272 available bytes; 98.30% used; 337540510 free inodes.
| server2 | True | ['4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 23036862464 available bytes; 98.71% used; 110407157 free inodes.

server2 `/home`: 23036862464 available bytes; 98.71% used; 110407157 free inodes.

server2 `/tmp`: 23036862464 available bytes; 98.71% used; 110407157 free inodes.

server2 `/var/tmp`: 23036862464 available bytes; 98.71% used; 110407157 free inodes.

server2 `/mnt/raid5`: 303442784256 available bytes; 97.90% used; 445057565 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84380274688 available bytes; 95.29% used; 114152622 free inodes.

server3 `/home`: 84380274688 available bytes; 95.29% used; 114152622 free inodes.

server3 `/data`: 127180767232 available bytes; 98.24% used; 225808132 free inodes.

server3 `/tmp`: 84380274688 available bytes; 95.29% used; 114152622 free inodes.

server3 `/var/tmp`: 84380274688 available bytes; 95.29% used; 114152622 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105664692224 available bytes; 94.10% used; 114349569 free inodes.

server4 `/home`: 105664692224 available bytes; 94.10% used; 114349569 free inodes.

server4 `/data`: 228734779392 available bytes; 96.84% used; 224928869 free inodes.

server4 `/tmp`: 105664692224 available bytes; 94.10% used; 114349569 free inodes.

server4 `/var/tmp`: 105664692224 available bytes; 94.10% used; 114349569 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
