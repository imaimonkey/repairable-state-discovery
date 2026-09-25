# V2R cluster inventory

2026-09-25T07:42:54.714696+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318864429056 available bytes; 82.21% used; 112480363 free inodes.

server1 `/home`: 318864429056 available bytes; 82.21% used; 112480363 free inodes.

server1 `/tmp`: 318864429056 available bytes; 82.21% used; 112480363 free inodes.

server1 `/var/tmp`: 318864429056 available bytes; 82.21% used; 112480363 free inodes.

server1 `/mnt/raid5`: 399598243840 available bytes; 98.17% used; 337558291 free inodes.
| server2 | True | ['0'] | [] |

server2 `/`: 22851964928 available bytes; 98.73% used; 110410511 free inodes.

server2 `/home`: 22851964928 available bytes; 98.73% used; 110410511 free inodes.

server2 `/tmp`: 22851964928 available bytes; 98.73% used; 110410511 free inodes.

server2 `/var/tmp`: 22851964928 available bytes; 98.73% used; 110410511 free inodes.

server2 `/mnt/raid5`: 334742917120 available bytes; 97.69% used; 445096095 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84438544384 available bytes; 95.29% used; 114156049 free inodes.

server3 `/home`: 84438544384 available bytes; 95.29% used; 114156049 free inodes.

server3 `/data`: 142391922688 available bytes; 98.03% used; 225812489 free inodes.

server3 `/tmp`: 84438544384 available bytes; 95.29% used; 114156049 free inodes.

server3 `/var/tmp`: 84438544384 available bytes; 95.29% used; 114156049 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105637453824 available bytes; 94.11% used; 114350349 free inodes.

server4 `/home`: 105637453824 available bytes; 94.11% used; 114350349 free inodes.

server4 `/data`: 249060745216 available bytes; 96.56% used; 225012398 free inodes.

server4 `/tmp`: 105637453824 available bytes; 94.11% used; 114350349 free inodes.

server4 `/var/tmp`: 105637453824 available bytes; 94.11% used; 114350349 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
