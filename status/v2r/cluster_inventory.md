# V2R cluster inventory

2026-09-24T08:16:10.944804+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324407914496 available bytes; 81.90% used; 112490613 free inodes.

server1 `/home`: 324407914496 available bytes; 81.90% used; 112490613 free inodes.

server1 `/tmp`: 324407914496 available bytes; 81.90% used; 112490613 free inodes.

server1 `/var/tmp`: 324407914496 available bytes; 81.90% used; 112490613 free inodes.

server1 `/mnt/raid5`: 495174131712 available bytes; 97.73% used; 337721347 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57818951680 available bytes; 96.77% used; 110431034 free inodes.

server2 `/home`: 57818951680 available bytes; 96.77% used; 110431034 free inodes.

server2 `/tmp`: 57818951680 available bytes; 96.77% used; 110431034 free inodes.

server2 `/var/tmp`: 57818951680 available bytes; 96.77% used; 110431034 free inodes.

server2 `/mnt/raid5`: 516576227328 available bytes; 96.43% used; 445180080 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85482455040 available bytes; 95.23% used; 114175150 free inodes.

server3 `/home`: 85482455040 available bytes; 95.23% used; 114175150 free inodes.

server3 `/data`: 175179837440 available bytes; 97.58% used; 225823306 free inodes.

server3 `/tmp`: 85482455040 available bytes; 95.23% used; 114175150 free inodes.

server3 `/var/tmp`: 85482455040 available bytes; 95.23% used; 114175150 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105778470912 available bytes; 94.10% used; 114349152 free inodes.

server4 `/home`: 105778470912 available bytes; 94.10% used; 114349152 free inodes.

server4 `/data`: 282306572288 available bytes; 96.10% used; 225350968 free inodes.

server4 `/tmp`: 105778470912 available bytes; 94.10% used; 114349152 free inodes.

server4 `/var/tmp`: 105778470912 available bytes; 94.10% used; 114349152 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
