# V2R cluster inventory

2026-09-27T02:37:04.592250+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315078447104 available bytes; 82.42% used; 112443400 free inodes.

server1 `/home`: 315078447104 available bytes; 82.42% used; 112443400 free inodes.

server1 `/tmp`: 315078447104 available bytes; 82.42% used; 112443400 free inodes.

server1 `/var/tmp`: 315078447104 available bytes; 82.42% used; 112443400 free inodes.

server1 `/mnt/raid5`: 637201887232 available bytes; 97.08% used; 337401568 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17628717056 available bytes; 99.02% used; 110365002 free inodes.

server2 `/home`: 17628717056 available bytes; 99.02% used; 110365002 free inodes.

server2 `/tmp`: 17628717056 available bytes; 99.02% used; 110365002 free inodes.

server2 `/var/tmp`: 17628717056 available bytes; 99.02% used; 110365002 free inodes.

server2 `/mnt/raid5`: 580770742272 available bytes; 95.99% used; 444884546 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78708314112 available bytes; 95.61% used; 114062955 free inodes.

server3 `/home`: 78708314112 available bytes; 95.61% used; 114062955 free inodes.

server3 `/data`: 1337679790080 available bytes; 81.51% used; 225762237 free inodes.

server3 `/tmp`: 78708314112 available bytes; 95.61% used; 114062955 free inodes.

server3 `/var/tmp`: 78708314112 available bytes; 95.61% used; 114062955 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111036182528 available bytes; 93.80% used; 114373249 free inodes.

server4 `/home`: 111036182528 available bytes; 93.80% used; 114373249 free inodes.

server4 `/data`: 400222076928 available bytes; 94.47% used; 224781487 free inodes.

server4 `/tmp`: 111036182528 available bytes; 93.80% used; 114373249 free inodes.

server4 `/var/tmp`: 111036182528 available bytes; 93.80% used; 114373249 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
